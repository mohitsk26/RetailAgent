import os
import streamlit as st
import requests
from rag.dynamic_ingest import process_uploaded_file

# ==========================================
# 1. PAGE SETUP & PREMIUM CSS
# ==========================================
st.set_page_config(
    page_title="RetailAgent AI",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Only keeping the essential CSS you requested for the premium card
st.markdown("""
<style>
.summary-card {
    background: #111827;
    padding: 20px;
    border-radius: 12px;
    border-left: 4px solid #8b5cf6;
    color: white;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
</style>
""", unsafe_allow_html=True)

st.title("🛒 RetailAgent AI")
st.markdown("Predictive Churn Copilot — diagnose risk and trigger retention strategies.")
st.divider()

# ==========================================
# 2. KNOWLEDGE BASE (RAG) UPLOAD
# ==========================================
st.subheader("📚 1. Knowledge Base Management")
uploaded_file = st.file_uploader(
    "Upload Business Documents (PDF, CSV, TXT, etc.) for Agent Context",
    type=["pdf", "docx", "txt", "md", "csv", "xlsx", "parquet"]
)

if uploaded_file:
    os.makedirs("uploads", exist_ok=True)
    save_path = os.path.join("uploads", uploaded_file.name)
    
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        
    with st.spinner("Processing document into vector chunks..."):
        total_chunks = process_uploaded_file(save_path)
        
    st.success(f"✅ RAG Knowledge Base Updated! ({total_chunks} chunks generated from {uploaded_file.name})")

st.divider()

# ==========================================
# 3. CUSTOMER PROFILE INPUTS
# ==========================================
st.subheader("👤 2. Customer Profile Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    recency = st.number_input("Recency (Days inactive)", min_value=0, value=95)
    avg_discount = st.number_input("Avg. Discount Applied (%)", min_value=0, value=25)

with col2:
    frequency = st.number_input("Frequency (Total orders)", min_value=0, value=3)
    customer_tier = st.selectbox("Customer Tier", ["Silver", "Gold", "Platinum"])

with col3:
    monetary = st.number_input("Monetary Value ($)", min_value=0, value=12000)
    favorite_category = st.selectbox("Favorite Category", ["Fashion", "Electronics", "Home", "Beauty", "Sports"])

st.write("") # Spacer

# ==========================================
# 4. API EXECUTION & RESULTS
# ==========================================
if st.button("🚀 Run Retention Analysis", use_container_width=True):
    
    # 1. Prepare data for the Machine Learning API
    payload = {
        "Recency": recency,
        "Frequency": frequency,
        "Monetary": monetary,
        "Avg_Discount": avg_discount,
        "Customer_Tier": customer_tier,
        "Favorite_Category": favorite_category
    }

    with st.spinner("Running ML prediction and LangGraph workflow..."):
        try:
            # 2. Send to FastAPI backend
            response = requests.post("http://127.0.0.1:8000/ai-recommendation", json=payload)

            if response.status_code == 200:
                result = response.json()
                st.divider()
                
                # 3. Explain the architecture step-by-step for the interviewer
                st.subheader("⚙️ How the AI Processed This:")
                summary = f"""
                * This customer has been inactive for **{recency} days** and has made only **{frequency} purchases**.
                * The Scikit-Learn Random Forest model predicts: **{result.get("risk")}**.
                * LangGraph routed the workflow based on that risk.
                * Relevant business knowledge was retrieved from the ChromaDB Vector database.
                * The LLM generated a retention strategy based on internal company policies.
                """
                st.info(summary)
                
                st.write("") # Spacer

                # 4. Display the Final Outputs
                out_col1, out_col2 = st.columns([1, 2])

                # LEFT BOX (Premium User Design)
                with out_col1:
                    st.markdown(f"""
                    <div class="summary-card">
                        <h4>🎯 Customer Risk Summary</h4>
                        <b>Risk Level:</b> {result.get("risk")}<br><br>
                        <b>Tier:</b> {customer_tier}<br>
                        <b>Category:</b> {favorite_category}<br>
                        <b>Recency:</b> {recency} days<br>
                        <b>Frequency:</b> {frequency} orders<br>
                        <b>Monetary:</b> ${monetary:,.0f}
                    </div>
                    """, unsafe_allow_html=True)

                # RIGHT BOX (Agent Strategy)
                with out_col2:
                    st.subheader("🤖 LangGraph Agent Strategy")
                    recommendation = result.get("recommendation", "No strategy recommendation provided.")
                    st.success(recommendation)

            else:
                st.error("Backend Error: Received an invalid status code from FastAPI.")

        except requests.exceptions.ConnectionError:
            st.error("Connection refused — make sure your FastAPI service is running on http://127.0.0.1:8000")
            
            # ==========================================
# 5. RAG AI CHAT
# ==========================================

st.divider()

st.subheader("💬 3. Ask AI About Uploaded Documents")

question = st.text_input(

    "Ask any business question",

    placeholder="Example: What is the refund policy?"

)

if st.button("🤖 Ask AI"):

    if question.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching Knowledge Base..."):

            try:

                response = requests.post(

                    "http://127.0.0.1:8000/chat",

                    json={

                        "query": question

                    }

                )

                if response.status_code == 200:

                    answer = response.json()["answer"]

                    st.success(answer)

                else:

                    st.error("Chat endpoint failed.")

            except requests.exceptions.ConnectionError:

                st.error("FastAPI backend is not running.")