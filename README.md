# RetailAgent - Agentic AI Customer Retention Copilot

# 1. Project Overview

## Introduction

RetailAgent is an Agentic AI-powered Customer Retention Copilot designed to help retail businesses identify customers who are likely to churn and automatically generate personalized retention recommendations using Machine Learning and Retrieval-Augmented Generation (RAG).

The project combines:

* Machine Learning
* FastAPI
* Chroma Vector Database
* HuggingFace Embeddings
* Retrieval-Augmented Generation (RAG)
* LangGraph Agent Orchestration
* Groq LLM

to create an enterprise-style AI Decision Support System.

Instead of simply predicting churn, RetailAgent predicts churn risk, retrieves business policies from the organization's knowledge base, and generates business-aware recommendations using multiple AI agents orchestrated by LangGraph.

---

# 2. Real World Problem

Retail companies lose millions every year due to customer churn.

Traditional systems only provide reports such as:

* Customer will churn
* Churn probability = 87%

but they do not answer:

* Why is the customer at risk?
* How should the company retain the customer?
* Which business policy should be applied?
* Which marketing strategy should be used?

RetailAgent solves this problem.

It predicts churn and immediately recommends retention strategies grounded in company knowledge.

---

# 3. Industrial Usage

This architecture can be deployed in:

* Amazon
* Flipkart
* Walmart
* Reliance Retail
* D-Mart
* E-commerce companies
* Telecom companies
* Banking sector
* Insurance sector
* Subscription platforms

Use cases:

* Customer retention
* Loyalty management
* Marketing automation
* Customer support copilot
* Call center assistant
* CRM assistant
* Personalized offers
* Sales recommendation engine

---

# 4. Business Benefits

* Reduces customer churn
* Improves customer lifetime value
* Reduces support costs
* Assists customer support executives
* Provides consistent recommendations
* Uses company-approved policies
* Minimizes hallucination through RAG
* Modular multi-agent architecture
* Easy to scale

---

# 5. Technology Stack

Backend

* Python
* FastAPI

Machine Learning

* Scikit-Learn
* RandomForestClassifier
* Pandas

RAG

* LangChain
* ChromaDB
* RecursiveCharacterTextSplitter
* HuggingFace Embeddings
* all-MiniLM-L6-v2

LLM

* Groq
* Llama-3.3-70B-Versatile

Agent Framework

* LangGraph

Model Storage

* Joblib

API Testing

* Swagger UI

---

# 6. End-to-End Architecture

Customer

↓

FastAPI

↓

LangGraph Supervisor

↓

Recommendation Agent

↓

Churn Agent → Random Forest

↓

Risk Prediction

↓

RAG Agent

↓

Retriever

↓

ChromaDB

↓

Knowledge Base

↓

Prompt Builder

↓

Groq LLM

↓

Business Recommendation

↓

JSON Response

---

# 7. Folder Structure

RetailAgent/

src/

api/

agents/

graph/

rag/

model/

config/

knowledge_base/

artifacts/

model/

data/

README.md

requirements.txt

.gitignore

.env.example

---

# 8. Project Phases

Phase 1

Project Initialization

* Virtual Environment
* Requirements
* Git
* Folder Structure

Phase 2

Data Cleaning

* Missing values
* Duplicates
* Standardization

Phase 3

Feature Engineering

* Recency
* Frequency
* Monetary
* Average Discount
* Customer Tier
* Favorite Category

Phase 4

Label Generation

Churn labels created using business rules.

Phase 5

Model Training

Random Forest

Reason:

* Handles nonlinear relationships
* Robust
* Feature importance
* Works well with mixed features

Phase 6

Encoding

OneHotEncoder

Reason:

Machine learning cannot process categorical strings.

Phase 7

Model Saving

joblib

Artifacts:

* churn_model.joblib
* preprocessor.joblib

Phase 8

FastAPI

Endpoints:

GET /

POST /predict

Phase 9

Knowledge Base

Markdown business documents

Policies

FAQs

SOP

Retention guidelines

Phase 10

Chunking

RecursiveCharacterTextSplitter

Purpose:

Large documents are divided into semantic chunks for better retrieval.

Phase 11

Embeddings

Sentence Transformer

all-MiniLM-L6-v2

Converts text into vectors.

Phase 12

ChromaDB

Stores vectors.

Enables semantic similarity search.

Phase 13

Retriever

Retrieves top-k relevant chunks.

Phase 14

Prompt Engineering

Context

*

Question

↓

Grounded Prompt

Phase 15

Groq LLM

Generates final grounded answer.

Phase 16

Agents

Churn Agent

RAG Agent

Recommendation Agent

Phase 17

LangGraph

Supervisor orchestrates all agents.

Phase 18

FastAPI AI Endpoint

POST /ai-recommendation

---

# 9. Why Random Forest?

Advantages

* Handles nonlinear patterns
* Robust to noise
* Good accuracy
* Less overfitting
* Feature importance
* Easy deployment

Alternative Models

* XGBoost
* LightGBM
* CatBoost
* Logistic Regression
* SVM

---

# 10. Why RAG?

Without RAG

LLM hallucinates.

With RAG

LLM answers only from company knowledge.

Benefits

* Updatable
* No retraining
* Grounded responses
* Lower hallucination

---

# 11. Why ChromaDB?

* Lightweight
* Local
* Fast similarity search
* Easy integration
* Good for portfolios

Alternatives

* Pinecone
* Weaviate
* Milvus
* FAISS

---

# 12. Why Embeddings?

Embeddings convert text into vectors.

Example:

"refund policy"

and

"return policy"

become mathematically close.

This enables semantic search.

---

# 13. Why LangGraph?

Traditional:

User

↓

One large function

↓

Answer

LangGraph:

User

↓

Supervisor

↓

Multiple specialized agents

↓

Final answer

Benefits:

* Modular
* Scalable
* Easy maintenance
* Enterprise architecture

---

# 14. Agent Design

Churn Agent

Predicts customer churn.

RAG Agent

Retrieves company knowledge.

Recommendation Agent

Combines ML + RAG.

LangGraph

Coordinates workflow.

---

# 15. API Endpoints

GET /

Health check

POST /predict

Returns:

prediction

risk

POST /ai-recommendation

Returns:

customer

risk

recommendation

---

# 16. Major Packages Used

fastapi

uvicorn

pandas

numpy

scikit-learn

joblib

langchain

langchain-chroma

langchain-huggingface

chromadb

sentence-transformers

langgraph

groq

python-dotenv

pydantic

---

# 17. Common Issues Faced

Gemini API

Issue:

503

Reason:

High demand

Solution:

Moved to Groq

---

Gemini quota

Issue:

429

Reason:

Free quota exhausted

Solution:

Used Groq

---

Groq

Issue:

401 Invalid API Key

Reason:

Incorrect key

Solution:

Generated new API key

---

Python package import

ModuleNotFoundError

Reason:

agent vs agents folder mismatch

Solution:

Correct module path

---

Environment variables

API key None

Reason:

.env not loaded

Solution:

load_dotenv(BASE_DIR / ".env")

---

Retriever quality

Chunks incomplete

Solution:

Increase chunk size and overlap

---

RAG hallucination

Prompt too weak

Solution:

Strict grounded prompt

---

FastAPI

Model path issue

Solution:

Use pathlib instead of relative strings

---

# 18. Future Improvements

* React dashboard
* Next.js frontend
* Authentication
* JWT
* PostgreSQL
* Redis caching
* Docker
* Kubernetes
* CI/CD
* Azure deployment
* AWS deployment
* Streaming responses
* Voice assistant
* Multi-language support
* Human approval workflow
* SQL Agent
* Analytics Agent
* Pricing Agent
* Inventory Agent
* Email Agent
* Fraud Detection Agent

---

# 19. UI Improvements

* Customer dashboard
* Charts
* KPI cards
* Churn probability gauge
* Customer timeline
* Recommendation history
* Download PDF report
* Chat interface
* Admin portal
* Analytics dashboard
* Live notifications
* Dark mode

---

# 20. Interview Highlights

This project demonstrates:

* Machine Learning
* FastAPI
* API Design
* RAG
* Vector Databases
* Embeddings
* Prompt Engineering
* Agentic AI
* LangGraph
* Multi-Agent Systems
* Production Architecture
* AI Decision Support Systems

It showcases the complete lifecycle from data preprocessing to AI-powered business recommendations.
