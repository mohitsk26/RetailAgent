
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

from src.graph.retail_graph import graph

import pandas as pd
import joblib

from pydantic import BaseModel

from src.rag.rag_chain import rag_pipeline

# ----------------------------------------------------
# Project Root
# ----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_DIR = BASE_DIR / "model"

# ----------------------------------------------------
# Load Model and Preprocessor
# ----------------------------------------------------

model = joblib.load(
    MODEL_DIR / "churn_model.joblib"
)

preprocessor = joblib.load(
    MODEL_DIR / "preprocessor.joblib"
)

# ----------------------------------------------------
# FastAPI App
# ----------------------------------------------------

app = FastAPI(
    title="RetailAgent AI API",
    description="Customer Churn Prediction + Agentic AI Recommendation System",
    version="1.0.0"
)

# ----------------------------------------------------
# Input Schema
# ----------------------------------------------------


class ChatRequest(BaseModel):

    query: str

class CustomerData(BaseModel):

    Recency: int

    Frequency: int

    Monetary: float

    Avg_Discount: float

    Customer_Tier: str

    Favorite_Category: str


# ----------------------------------------------------
# Home Endpoint
# ----------------------------------------------------

@app.get("/")

def home():

    return {

        "message": "RetailAgent AI API is running successfully.",

        "available_endpoints": [

            "/predict",

            "/ai-recommendation",

            "/docs"

        ]

    }


# ----------------------------------------------------
# ML Prediction Endpoint
# ----------------------------------------------------

@app.post("/predict")

def predict(customer: CustomerData):

    input_df = pd.DataFrame(

        [

            {

                "Recency": customer.Recency,

                "Frequency": customer.Frequency,

                "Monetary": customer.Monetary,

                "Avg_Discount": customer.Avg_Discount,

                "Customer_Tier": customer.Customer_Tier,

                "Favorite_Category": customer.Favorite_Category,

            }

        ]

    )

    transformed_data = preprocessor.transform(

        input_df

    )

    prediction = model.predict(

        transformed_data

    )[0]

    return {

        "prediction": int(prediction),

        "risk": (

            "High Churn"

            if prediction == 1

            else "Low Churn"

        )

    }


# ----------------------------------------------------
# LangGraph AI Recommendation Endpoint
# ----------------------------------------------------

@app.post("/ai-recommendation")

def ai_recommendation(customer: CustomerData):

    customer_dict = {

        "Recency": customer.Recency,

        "Frequency": customer.Frequency,

        "Monetary": customer.Monetary,

        "Avg_Discount": customer.Avg_Discount,

        "Customer_Tier": customer.Customer_Tier,

        "Favorite_Category": customer.Favorite_Category,

    }

    result = graph.invoke(

        {

            "customer": customer_dict

        }

    )

    return {

        "customer": customer_dict,

        "risk": result["result"]["risk"],

        "recommendation": result["result"]["recommendation"]

    }


@app.post("/chat")

def chat(request: ChatRequest):

    answer = rag_pipeline(

        request.query

    )

    return {

        "answer": answer

    }