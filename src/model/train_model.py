import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

from sklearn.preprocessing import OneHotEncoder

from sklearn.compose import ColumnTransformer

import joblib

def load_dataset():

    df = pd.read_csv(
        "data/processed/labeled_rfm_dataset.csv"
    )

    return df


def split_features_target(df):

    X = df[
    [
        "Recency",
        "Frequency",
        "Monetary",
        "Avg_Discount",
        "Customer_Tier",
        "Favorite_Category"
    ]
]

    y = df["Churn"]

    return X, y

def encode_features(X_train, X_test):

    categorical_columns = [

        "Customer_Tier",

        "Favorite_Category"

    ]

    preprocessor = ColumnTransformer(

        transformers=[

            (

                "cat",

                OneHotEncoder(

                    handle_unknown="ignore"

                ),

                categorical_columns

            )

        ],

        remainder="passthrough"

    )

    X_train = preprocessor.fit_transform(

        X_train

    )

    X_test = preprocessor.transform(

        X_test

    )

    return X_train, X_test, preprocessor



def split_train_test(X, y):

    X_train, X_test, y_train, y_test = train_test_split(

        X,

        y,

        test_size=0.2,

        random_state=42,

        stratify=y

    )

    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):

    model = RandomForestClassifier(

        random_state=42,

        class_weight="balanced"

    )

    model.fit(

        X_train,

        y_train

    )

    return model

def make_predictions(model, X_test):

    y_pred = model.predict(
        X_test
    )

    return y_pred

def evaluate_model(y_test, y_pred):

    print("\nAccuracy:")

    print(
        accuracy_score(
            y_test,
            y_pred
        )
    )

    print("\nPrecision:")

    print(
        precision_score(
            y_test,
            y_pred
        )
    )

    print("\nRecall:")

    print(
        recall_score(
            y_test,
            y_pred
        )
    )

    print("\nF1 Score:")

    print(
        f1_score(
            y_test,
            y_pred
        )
    )

    print("\nConfusion Matrix:")

    print(
        confusion_matrix(
            y_test,
            y_pred
        )
    )

    print("\nClassification Report:")

    print(
        classification_report(
            y_test,
            y_pred
        )
    )
    
def save_model(model, preprocessor):

    import os

    os.makedirs(
        "model",
        exist_ok=True
    )

    joblib.dump(

        model,

        "model/churn_model.joblib"

    )

    joblib.dump(

        preprocessor,

        "model/preprocessor.joblib"

    )

    print(

        "\n✅ Model and preprocessor saved successfully."

    )

if __name__ == "__main__":

    df = load_dataset()

    X, y = split_features_target(df)

    X_train, X_test, y_train, y_test = split_train_test(
        X,
        y
    )

    X_train, X_test, preprocessor = encode_features(
        X_train,
        X_test
    )

    model = train_model(
        X_train,
        y_train
    )

    y_pred = make_predictions(
        model,
        X_test
    )

    print("\nModel trained successfully.")

    print("\nFirst 10 Predictions:")

    print(y_pred[:10])

    evaluate_model(
        y_test,
        y_pred
    )
    
    save_model(
    model,
    preprocessor
    )