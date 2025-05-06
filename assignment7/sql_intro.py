import sqlite3
import pandas as pd

# Task 1–4
def database():
    try:
        with sqlite3.connect("../db/magazines.db") as conn:
            conn.execute("PRAGMA foreign_keys = 1")  # Required for foreign key checks
            print("Database connected successfully")
            cursor = conn.cursor()

            # Create tables
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS publishers(
               publisher_id INTEGER PRIMARY KEY,
               name TEXT NOT NULL UNIQUE         
            )""")

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS magazines(
               magazine_id INTEGER PRIMARY KEY,
               name TEXT NOT NULL UNIQUE, 
               publisher_id INTEGER NOT NULL,
               FOREIGN KEY(publisher_id) REFERENCES publishers(publisher_id)
            )""")

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscribers(
               subscriber_id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,    
               address TEXT NOT NULL            
            )""")

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions(
               subscription_id INTEGER PRIMARY KEY,
               subscriber_id INTEGER NOT NULL,
               magazine_id INTEGER NOT NULL,
               expiration_date TEXT NOT NULL,
               FOREIGN KEY(subscriber_id) REFERENCES subscribers(subscriber_id),
               FOREIGN KEY(magazine_id) REFERENCES magazines(magazine_id)                             
            )""")

            print('Tables created')

            # Functions to insert data
            def add_publisher(cursor, name):
                try:
                    cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
                except sqlite3.IntegrityError:
                    pass

            def add_magazine(cursor, name, publisher_id):
                try:
                    cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id,))
                except sqlite3.IntegrityError:
                    pass

            def add_subscriber(cursor, name, address):
                cursor.execute("SELECT 1 FROM subscribers WHERE name = ? AND address = ?", (name, address))
                if not cursor.fetchone():
                    cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))

            def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
                try:
                    cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
                                   (subscriber_id, magazine_id, expiration_date,))
                except sqlite3.IntegrityError:
                    pass

            # Sample data
            add_publisher(cursor, "Penguin House")
            add_publisher(cursor, "Pearson")
            add_publisher(cursor, "Fluffy")

            add_magazine(cursor, "Javascript", 1)
            add_magazine(cursor, "Tech", 2)
            add_magazine(cursor, "Dogs", 3)

            add_subscriber(cursor, "Alice", "123 Main St")
            add_subscriber(cursor, "Bob", "456 Oak Ave")
            add_subscriber(cursor, "Alice", "789 Pine Rd")

            add_subscription(cursor, 1, 1, "2025-12-31")
            add_subscription(cursor, 2, 2, "2025-11-30")
            add_subscription(cursor, 3, 3, "2026-01-15")

            conn.commit()
            print("Sample data inserted successfully.")

            # Task 4: Queries
            print('\nAll Subscribers:')
            cursor.execute('SELECT * FROM subscribers')
            for subscriber in cursor.fetchall():
                print(subscriber)

            print('\nAll Magazines (sorted by name):')
            cursor.execute('SELECT * FROM magazines ORDER BY name')
            for magazine in cursor.fetchall():
                print(magazine)

            print('\nMagazines published by Penguin House:')
            cursor.execute("""
                SELECT m.magazine_id, m.name, p.name as publisher_name
                FROM magazines m
                JOIN publishers p ON m.publisher_id = p.publisher_id
                WHERE p.name = 'Penguin House'
            """)
            for row in cursor.fetchall():
                print(row)

    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")

database()
