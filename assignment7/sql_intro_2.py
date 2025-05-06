import sqlite3
import pandas as pd

# Connect to the lesson database
with sqlite3.connect("../db/lesson.db") as conn:
    # Read data into DataFrame using JOIN
    df = pd.read_sql_query("""
        SELECT 
            line_items.line_item_id,
            line_items.quantity,
            line_items.product_id,
            products.product_name,
            products.price
        FROM line_items
        JOIN products ON line_items.product_id = products.product_id
    """, conn)

    # Print first 5 rows
    print("Initial DataFrame (first 5 rows):")
    print(df.head())

    # Add "total" column
    df['total'] = df['quantity'] * df['price']
    print("\nWith 'total' column (first 5 rows):")
    print(df.head())

    # Group by product_id and summarize
    summary = df.groupby('product_id').agg({
        'line_item_id': 'count',
        'total': 'sum',
        'product_name': 'first'
    }).reset_index()

    # Sort by product_name
    summary = summary.sort_values('product_name')

    print("\nSummary grouped by product:")
    print(summary.head())

    # Save to CSV
    summary.to_csv("order_summary.csv", index=False)
    print("\nSaved summary to 'order_summary.csv'")
    