import pandas as pd

def load_transactions():
    

    df = pd.read_csv(
        "data/raw/transactions.csv"
    )

    return df

def inspect_data(df):

    print("\nDataset Shape:")
    print(df.shape)

    print("\nDataset Information:")
    df.info()

    print("\nMissing Values:")
    print(df.isnull().sum())


def convert_purchase_date(df):

    df["purchase_date"] = pd.to_datetime(
        df["purchase_date"]
    )

    return df

def remove_duplicates(df):

    before_count = len(df)

    df = df.drop_duplicates()

    after_count = len(df)

    print(
        f"\nRemoved {before_count - after_count} duplicate rows."
    )

    return df

def validate_numeric_columns(df):

    assert (
        df["quantity"] > 0
    ).all(), "Invalid quantity found."

    assert (
        df["unit_price"] > 0
    ).all(), "Invalid unit price found."

    assert (
        df["discount_given"].between(0, 30)
    ).all(), "Invalid discount found."

    assert (
        df["sales_amount"] >= 0
    ).all(), "Invalid sales amount found."

    print(
        "\nBusiness rule validation passed."
    )

    return df


def save_clean_data(df):

    df.to_csv(
        "data/processed/clean_transactions.csv",
        index=False
    )

    print(
        "\nClean dataset saved successfully."
    )

    return df

if __name__ == "__main__":

    df = load_transactions()

    inspect_data(df)

    df = convert_purchase_date(df)
    
    df = remove_duplicates(df)
    
    df = validate_numeric_columns(df)

    df = save_clean_data(df)
    
    print("\nCleaning pipeline completed successfully.")

    print(df.dtypes)