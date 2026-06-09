from src.agents.churn_agent import predict_churn
from src.agents.rag_agent import rag_answer


def generate_recommendation(customer_data: dict):

    # -------------------------
    # ML Prediction
    # -------------------------

    churn_result = predict_churn(
        customer_data
    )

    # -------------------------
    # Decide RAG Query
    # -------------------------

    if churn_result["prediction"] == 1:

        query = (
            "How should I retain a high churn customer?"
        )

    else:

        query = (
            "How should I engage a low churn customer?"
        )

    # -------------------------
    # RAG
    # -------------------------

    rag_result = rag_answer(query)

    # -------------------------
    # Final Response
    # -------------------------

    return {

        "risk": churn_result["risk"],

        "recommendation": rag_result["answer"]

    }


if __name__ == "__main__":

    customer = {

        "Recency": 95,

        "Frequency": 3,

        "Monetary": 12000,

        "Avg_Discount": 25,

        "Customer_Tier": "Silver",

        "Favorite_Category": "Fashion"

    }

    result = generate_recommendation(
        customer
    )

    print("=" * 80)

    print("FINAL RECOMMENDATION")

    print("=" * 80)

    print(result)