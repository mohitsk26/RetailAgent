import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd


PRODUCT_CATEGORIES = {
    "Electronics": [
        "Laptop",
        "Smartphone",
        "Headphones",
        "Smart Watch"
    ],
    "Fashion": [
        "T-Shirt",
        "Jeans",
        "Jacket",
        "Shoes"
    ],
    "Groceries": [
        "Rice",
        "Milk",
        "Bread",
        "Eggs"
    ],
    "Home Decor": [
        "Lamp",
        "Curtains",
        "Wall Art",
        "Carpet"
    ],
    "Sports": [
        "Football",
        "Cricket Bat",
        "Yoga Mat",
        "Dumbbells"
    ],
    "Beauty": [
        "Face Wash",
        "Perfume",
        "Shampoo",
        "Moisturizer"
    ]
}

CUSTOMER_TIERS = [
    "Silver",
    "Gold",
    "Platinum"
]

CITIES = [
    "Pune",
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Hyderabad",
    "Chennai"
]

PAYMENT_METHODS = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Wallet"
]



CATEGORY_PRICE_RANGES = {
    "Electronics": (5000, 50000),
    "Fashion": (500, 5000),
    "Groceries": (100, 2000),
    "Home Decor": (1000, 10000),
    "Sports": (500, 8000),
    "Beauty": (200, 5000)
}

TIER_PURCHASE_MULTIPLIER = {
    "Silver": 1.0,
    "Gold": 1.5,
    "Platinum": 2.0
}



def generate_transaction_record():
    
    customer_id = f"C{random.randint(1001, 2000)}"

    customer_tier = random.choice(CUSTOMER_TIERS)

    city = random.choice(CITIES)

    payment_method = random.choice(PAYMENT_METHODS)

    product_category = random.choice(
        list(PRODUCT_CATEGORIES.keys())
    )

    product_name = random.choice(
        PRODUCT_CATEGORIES[product_category]
    )
    
    quantity = random.randint(1, 5)

    min_price, max_price = CATEGORY_PRICE_RANGES[
        product_category
    ]

    base_price = random.randint(
        min_price,
        max_price
    )

    unit_price = int(
        base_price *
        TIER_PURCHASE_MULTIPLIER[customer_tier]
    )

    discount_given = random.randint(0, 30)
    
    order_id = f"O{random.randint(10001, 99999)}"

    days_ago = random.randint(0, 365)

    purchase_date = (
        datetime.now() -
        timedelta(days=days_ago)
    ).date()
    
    
    sales_amount = (
        quantity *
        unit_price *
        (1 - discount_given / 100)
    )
    
    return {
        "customer_id": customer_id,
        "order_id": order_id,
        "purchase_date": purchase_date,
        "product_category": product_category,
        "product_name": product_name,
        "quantity": quantity,
        "unit_price": unit_price,
        "discount_given": discount_given,
        "sales_amount": round(sales_amount, 2),
        "customer_tier": customer_tier,
        "city": city,
        "payment_method": payment_method
    }
def generate_dataset():
    transactions = []
    for _ in range(10000):
        transactions.append(
            generate_transaction_record()
        )

    df = pd.DataFrame(transactions)

    df.to_csv(
        "data/raw/transactions.csv",
        index=False
    )

    print(
        "Dataset saved to data/raw/transactions.csv"
    )

    return df


if __name__ == "__main__":
    df = generate_dataset()
    print(df.head())
    
    
# Example Output

# Later:

# generate_transaction_record()

# might return:

# {
#     "customer_id": "C1458",
#     "order_id": "O71234",
#     "purchase_date": "2026-02-11",
#     "product_category": "Electronics",
#     "product_name": "Laptop",
#     "quantity": 2,
#     "unit_price": 25000,
#     "discount_given": 10,
#     "sales_amount": 45000,
#     "customer_tier": "Gold",
#     "city": "Pune",
#     "payment_method": "UPI"
# }



# Important Question
# Why return a dictionary instead of a list?

# Because:

# Dictionary

# preserves:

# column names

# Example:

# {
#     "customer_id": "C1001"
# }

# is self-describing.

# A list:

# ["C1001", "Gold", "Pune"]

# has no meaning without documentation.