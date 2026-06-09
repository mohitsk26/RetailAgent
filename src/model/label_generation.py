import random

import pandas as pd

from src.config.settings import (
    CHURN_RECENCY_THRESHOLD,
    CHURN_FREQUENCY_THRESHOLD,
    CHURN_MONETARY_THRESHOLD
)




def load_rfm_data():

    rfm_df = pd.read_csv(
        "data/processed/rfm_dataset.csv"
    )

    return rfm_df


# Why create a separate load_rfm_data() function
# instead of calling pd.read_csv() directly?

#  Answer:

# Encapsulating file loading
# in a dedicated function improves maintainability,
# reduces code duplication, and allows future changes 
# to the data source without affecting the rest of the pipeline.

def generate_churn_labels(rfm_df):

    risk_score = (

        (
            rfm_df["Recency"] > 60
        ).astype(int) * 30

        +

        (
            rfm_df["Frequency"] < 8
        ).astype(int) * 20

        +

        (
            rfm_df["Monetary"] < 50000
        ).astype(int) * 20

        +

        (
            rfm_df["Customer_Tier"] == "Silver"
        ).astype(int) * 10

        +

        (
            rfm_df["Avg_Discount"] > 20
        ).astype(int) * 10

        +

        (
            rfm_df["Favorite_Category"].isin(
                [
                    "Fashion",
                    "Beauty"
                ]
            )
        ).astype(int) * 10

    )

    rfm_df["Risk_Score"] = risk_score


    def assign_churn(risk):

        if risk >= 70:

            return 1 if random.random() < 0.85 else 0

        elif risk >= 50:

            return 1 if random.random() < 0.50 else 0

        else:

            return 1 if random.random() < 0.10 else 0


    rfm_df["Churn"] = (

        rfm_df["Risk_Score"]

        .apply(assign_churn)

    )

    return rfm_df



# Why convert boolean values to integers?

# Strong Answer:

# The business rule produces boolean values (True/False), 
# but supervised classification models expect numeric
# target labels.
# Converting them to 1 and 0 creates a standard binary 
# classification target.


def save_labeled_dataset(rfm_df):

    rfm_df.to_csv(
        "data/processed/labeled_rfm_dataset.csv",
        index=False
    )

    print(
        "\nLabeled RFM dataset saved successfully."
    )

    return rfm_df


if __name__ == "__main__":

    rfm_df = load_rfm_data()

    rfm_df = generate_churn_labels(
        rfm_df
    )

    save_labeled_dataset(
        rfm_df
    )

    print(
        "\nLabeled Dataset Preview:"
    )

    print(
        rfm_df.head()
    )

    print(
        "\nChurn Distribution:"
    )

    print(
        rfm_df["Churn"].value_counts()
    )
    
    
    
    
    
# Why inspect the target distribution before model training?


# Strong Answer:

# Inspecting the target distribution 
# helps identify class imbalance. 
# Highly imbalanced datasets
# can bias the model toward the majority class
# and may require techniques 
# such as class weighting, oversampling,
# or different evaluation metrics.


# Is 99.8% accuracy always good?

# Strong Answer:

# No. On highly imbalanced datasets,
# a model can achieve high accuracy by 
# always predicting the majority class.
# In such cases, metrics like Precision, Recall, F1-score,
# and ROC-AUC are more informative than accuracy alone.


# Your churn dataset is imbalanced. What would you do?
# Strong Answer

# I would first inspect the class distribution and 
# evaluate whether the imbalance reflects
# real business behavior. During model training,
# I could use techniques such as class_weight="balanced", 
# SMOTE, or Random Over Sampling if needed.
# I would also prioritize Precision, Recall, 
# and F1-score over Accuracy for evaluation.

# This answer is excellent for interviews.




# we did changed the business rule 
# and successfully generated the labeled dataset: , 
# give me a brief on it , how ,
# where and what we did on which step , 
# file, and function and why