import pandas as pd

def load_clean_data():

    df = pd.read_csv(
        "data/processed/clean_transactions.csv"
    )

    df["purchase_date"] = pd.to_datetime(
        df["purchase_date"]
    )

    return df

def calculate_recency(df):

    reference_date = df[
        "purchase_date"
    ].max()

    recency = (

        df.groupby(
            "customer_id"
        )["purchase_date"]

        .max()

        .apply(

            lambda x:
            (
                reference_date - x
            ).days

        )

    )

    return recency



def calculate_frequency(df):

    frequency = (

        df.groupby(
            "customer_id"
        )["order_id"]

        .count()

    )

    return frequency

def calculate_monetary(df):

    monetary = (

        df.groupby(
            "customer_id"
        )["sales_amount"]

        .sum()

    )

    return monetary



def build_rfm_table(df):

    recency = calculate_recency(df)

    frequency = calculate_frequency(df)

    monetary = calculate_monetary(df)

    customer_tier = (

        df.groupby(
            "customer_id"
        )["customer_tier"]

        .agg(
            lambda x: x.mode()[0]
        )

    )

    avg_discount = (

        df.groupby(
            "customer_id"
        )["discount_given"]

        .mean()

    )

    favorite_category = (

        df.groupby(
            "customer_id"
        )["product_category"]

        .agg(
            lambda x: x.mode()[0]
        )

    )

    rfm_df = pd.concat(

        [
            recency,
            frequency,
            monetary,
            customer_tier,
            avg_discount,
            favorite_category
        ],

        axis=1

    )

    rfm_df.columns = [

        "Recency",

        "Frequency",

        "Monetary",

        "Customer_Tier",

        "Avg_Discount",

        "Favorite_Category"

    ]

    return rfm_df

def save_rfm_dataset(rfm_df):

    rfm_df.to_csv(
        "data/processed/rfm_dataset.csv"
    )

    print(
        "\nRFM dataset saved successfully."
    )

    return rfm_df



if __name__ == "__main__":

    df = load_clean_data()

    rfm_df = build_rfm_table(df)

    save_rfm_dataset(rfm_df)

    print("\nRFM Dataset Preview:")

    print(rfm_df.head())