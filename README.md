# 🛒 RetailAgent AI – Intelligent Customer Churn Prediction & Retention Copilot

## 🚀 Project Overview

RetailAgent AI is an enterprise-inspired intelligent retail decision support system that combines **Machine Learning, Retrieval-Augmented Generation (RAG), Agentic AI, LangGraph orchestration, Vector Search, and Large Language Models** to help businesses proactively retain customers.

Unlike traditional churn prediction systems that only identify customers at risk of leaving, RetailAgent AI completes the entire business workflow by predicting churn, retrieving organizational knowledge, and generating actionable retention strategies based on dynamically uploaded business policies.

---

# 🎯 Business Problem

Retail organizations lose millions of dollars annually due to customer churn.

Traditional ML models answer:

> **Which customer is likely to churn?**

But businesses also need to know:

* What should we do to retain this customer?
* Which company policy should be followed?
* What is the latest retention strategy?
* How can business teams update recommendations without retraining AI models?

RetailAgent AI addresses these challenges by combining predictive analytics with dynamic knowledge retrieval.

---

# 💡 Solution

RetailAgent AI integrates:

* Predictive Machine Learning
* Retrieval-Augmented Generation (RAG)
* Agent-based orchestration
* Dynamic document ingestion
* Semantic vector search
* Enterprise APIs
* Interactive dashboard

to create an intelligent AI-powered retail copilot.

---

# 🏗️ End-to-End Architecture

```text
                        Streamlit Dashboard
                                │
                ┌───────────────┴────────────────┐
                │                                │
         Upload Business Docs            Customer Metrics
                │                                │
                ▼                                ▼
      Dynamic Document Loader             FastAPI Endpoint
                │                                │
                ▼                                ▼
      Recursive Text Splitter          Feature Preprocessing
                │                                │
                ▼                                ▼
     MiniLM Embedding Model          Random Forest Model
                │                                │
                ▼                                ▼
            ChromaDB Vector Store      Churn Prediction
                │                                │
                └───────────────┬────────────────┘
                                │
                           LangGraph
                                │
               ┌────────────────┴───────────────┐
               │                                │
        Churn Agent                  Recommendation Agent
               │                                │
               └──────────────┬─────────────────┘
                              │
                         RAG Pipeline
                              │
                       Semantic Retrieval
                              │
                          Groq LLM
                              │
                     Personalized Strategy
                              │
                              ▼
                    Streamlit User Interface
```

---

# ⚙️ Working Flow

## Phase 1 — Customer Data Collection

Customer metrics are collected through the Streamlit dashboard.

* Recency
* Frequency
* Monetary Value
* Average Discount
* Customer Tier
* Favorite Category

In production, these values would be fetched automatically from CRM and transactional databases.

---

## Phase 2 — Churn Prediction

The customer profile is sent to FastAPI.

FastAPI loads:

* preprocessor.joblib
* churn_model.joblib

The data is transformed using the same preprocessing pipeline used during training.

The Random Forest model predicts:

* High Churn
* Low Churn

---

## Phase 3 — Agent Orchestration

Instead of returning only the prediction, LangGraph orchestrates the workflow.

It coordinates specialized agents:

* Churn Agent
* Recommendation Agent
* RAG Agent

Each agent performs an isolated responsibility, making the architecture modular and scalable.

---

## Phase 4 — Retrieval-Augmented Generation

The RAG agent queries the knowledge base.

Documents uploaded by business users are:

* Loaded
* Chunked
* Embedded
* Stored in ChromaDB

The retriever performs semantic similarity search and returns the most relevant chunks.

These chunks are combined with the user query and passed to the LLM.

---

## Phase 5 — Intelligent Recommendation

The Groq-hosted LLM generates a grounded response using retrieved company policies instead of hallucinating.

This produces personalized retention strategies aligned with organizational business rules.

---

# 📚 Dynamic Knowledge Base

Supported document formats:

* PDF
* DOCX
* TXT
* Markdown
* CSV
* Excel
* Parquet

New business policies can be uploaded at runtime without retraining the ML model.

---

# 🧠 Core Concepts Used

* Machine Learning
* Customer Churn Prediction
* Random Forest Classifier
* Feature Engineering (RFM)
* One-Hot Encoding
* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Databases
* Embeddings
* ChromaDB
* LangGraph
* Agentic AI
* Prompt Engineering
* FastAPI
* Streamlit
* Dynamic Knowledge Ingestion

---

# 🛠️ Tech Stack

### Programming

* Python

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy

### Generative AI

* Groq API
* Llama 3.3 70B

### RAG

* LangChain
* ChromaDB
* HuggingFace Embeddings
* RecursiveCharacterTextSplitter

### Agent Framework

* LangGraph

### Backend

* FastAPI
* Pydantic

### Frontend

* Streamlit

### Model Persistence

* Joblib

---

# 🌍 Real-World Retail Use Cases

* Customer retention
* Loyalty optimization
* Marketing campaign personalization
* Dynamic policy consultation
* Customer support automation
* AI sales assistant
* CRM augmentation
* Executive decision support

---

# 💼 Business Benefits

* Reduces customer churn
* Improves customer lifetime value
* Eliminates manual policy lookup
* Enables zero-downtime policy updates
* Reduces operational costs
* Improves support team productivity
* Delivers personalized retention strategies

---

# 🚀 Why This Architecture?

Traditional systems:

Predict churn → Human decides action.

RetailAgent AI:

Predict churn → Retrieve latest business knowledge → Generate personalized strategy.

This separates predictive analytics from business logic, reducing maintenance effort and enabling rapid policy updates.

---

# 🔥 Key Innovation

Marketing teams can update AI behavior by simply uploading a new policy document.

No code changes.

No model retraining.

No application redeployment.

The AI instantly adapts using Retrieval-Augmented Generation.

---

# 📈 Future Enhancements

* Customer authentication
* Real-time CRM integration
* Kafka event streaming
* Spark batch analytics
* Voice-enabled assistant
* Multi-agent collaboration
* Azure OpenAI integration
* Recommendation ranking engine
* Customer sentiment analysis
* Explainable AI dashboard
* Role-based access control
* Cloud deployment on Azure/AWS

---

# 🎯 Industry Relevance

RetailAgent AI demonstrates an enterprise-grade architecture combining predictive analytics, vector databases, semantic retrieval, agent orchestration, and LLM reasoning.

It showcases how modern AI systems can bridge the gap between machine learning predictions and business decision-making, making it highly relevant for Retail, E-commerce, Banking, Insurance, Telecommunications, and Customer Experience platforms.

---

# 👨‍💻 Project by

**Mohit Singh Kashyap**

AI • Machine Learning • Data Engineering • Generative AI • RAG • LangGraph • FastAPI • Streamlit
