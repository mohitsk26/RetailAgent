import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

import os

print(os.getcwd())


def load_clean_data():

    df = pd.read_csv(
        "data/processed/clean_transactions.csv",
        parse_dates=["purchase_date"]
    )

    return df

def spending_distribution(df):

    plt.figure(figsize=(10, 6))

    plt.hist(
        df["sales_amount"],
        bins=30
    )

    plt.title(
        "Customer Spending Distribution"
    )

    plt.xlabel(
        "Sales Amount"
    )

    plt.ylabel(
        "Number of Transactions"
    )

    plt.savefig(
        "outputs/charts/spending_distribution.png"
    )

    plt.close()

    print(
        "Spending distribution chart saved."
    )


def sales_by_category(df):

    category_sales = (
        df.groupby(
            "product_category"
        )["sales_amount"].sum()
    )

    plt.figure(figsize=(10, 6))

    category_sales.plot(
        kind="bar"
    )

    plt.title(
        "Sales by Product Category"
    )

    plt.xlabel(
        "Product Category"
    )

    plt.ylabel(
        "Total Sales"
    )

    plt.savefig(
        "outputs/charts/category_sales.png"
    )

    plt.close()

    print(
        "Category sales chart saved."
    )

    return category_sales  

def customer_tier_distribution(df):

    tier_counts = (
        df["customer_tier"]
        .value_counts()
    )

    plt.figure(figsize=(8, 6))

    tier_counts.plot(
        kind="bar"
    )

    plt.title(
        "Customer Tier Distribution"
    )

    plt.xlabel(
        "Customer Tier"
    )

    plt.ylabel(
        "Number of Transactions"
    )

    plt.savefig(
        "outputs/charts/customer_tier_distribution.png"
    )

    plt.close()

    print(
        "Customer tier distribution chart saved."
    )

    return tier_counts


def revenue_by_city(df):

    city_sales = (
        df.groupby(
            "city"
        )["sales_amount"].sum()
    )

    plt.figure(figsize=(10, 6))

    city_sales.plot(
        kind="bar"
    )

    plt.title(
        "Revenue by City"
    )

    plt.xlabel(
        "City"
    )

    plt.ylabel(
        "Total Revenue"
    )

    plt.savefig(
        "outputs/charts/revenue_by_city.png"
    )

    plt.close()

    print(
        "Revenue by city chart saved."
    )

    return city_sales

def monthly_sales_trend(df):

    monthly_sales = (
        df.groupby(
            df["purchase_date"].dt.to_period("M")
        )["sales_amount"].sum()
    )

    plt.figure(figsize=(10, 6))

    monthly_sales.plot(
        kind="line",
        marker="o"
    )

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        "outputs/charts/monthly_sales_trend.png"
    )

    plt.close()

    print("Monthly sales trend chart saved.")

    return monthly_sales

def correlation_heatmap(df):

    numeric_df = df.select_dtypes(
        include="number"
    )

    correlation_matrix = numeric_df.corr()

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap="coolwarm"
    )

    plt.title(
        "Feature Correlation Heatmap"
    )

    plt.savefig(
        "outputs/charts/correlation_heatmap.png"
    )

    plt.close()

    print(
        "Correlation heatmap saved."
    )

    return correlation_matrix
    
if __name__ == "__main__":

    df = load_clean_data()

    spending_distribution(df)
    
    sales_by_category(df)
    
    customer_tier_distribution(df)
    
    revenue_by_city(df)
    
    monthly_sales_trend(df)
    
    correlation_heatmap(df)