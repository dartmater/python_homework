import sqlite3

def task1():
    try:
        conn = sqlite3.connect(r"C:\Users\lnpov\Documents\CTD_Project\python_class\python_homework\db\lesson.db")
        cursor = conn.cursor()
        query = """
        SELECT 
            o.order_id,
            SUM(p.price * li.quantity) AS total_price
        FROM 
            orders o
        JOIN 
            line_items li ON o.order_id = li.order_id
        JOIN 
            products p ON li.product_id = p.product_id
        GROUP BY 
            o.order_id
        ORDER BY 
            o.order_id
        LIMIT 5;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        print("Task 1: Total price of first 5 orders")
        for order_id, total_price in results:
            print(f"Order ID: {order_id}, Total Price: ${total_price}")
    except sqlite3.Error as e:
        print(f"Database error in task1: {e}")
    finally:
       
            conn.close()

def task2():
    try:
        conn = sqlite3.connect(r"C:\Users\lnpov\Documents\CTD_Project\python_class\python_homework\db\lesson.db")
        cursor = conn.cursor()
        query = """
        SELECT c.customer_name, AVG(total_price) AS average_price
        FROM (
            SELECT o.customer_id AS customer_id_b, SUM(p.price * li.quantity) AS total_price
            FROM orders o
            JOIN line_items li ON o.order_id = li.order_id
            JOIN products p ON li.product_id = p.product_id
            GROUP BY o.order_id
        ) subq
        LEFT JOIN customers c ON subq.customer_id_b = c.customer_id
        GROUP BY c.customer_id;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        print("\nTask 2: Average order prices by customer:")
        for customer_name, avg_price in results:
            print(f"Customer: {customer_name}, AVG: ${avg_price:.2f}")
    except sqlite3.Error as e:
        print(f"Database error in task2: {e}")
    finally:
       
            conn.close()

def task3():
    try:
        conn = sqlite3.connect(r"C:\Users\lnpov\Documents\CTD_Project\python_class\python_homework\db\lesson.db")
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        # Get required IDs
        cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
        customer_id = cursor.fetchone()[0]

        cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'")
        employee_id = cursor.fetchone()[0]

        cursor.execute("SELECT product_id FROM products ORDER BY price LIMIT 5")
        product_ids = [row[0] for row in cursor.fetchall()]

        # Start transaction
        cursor.execute(
            "INSERT INTO orders (customer_id, employee_id) VALUES (?, ?) RETURNING order_id",
            (customer_id, employee_id)
        )
        order_id = cursor.fetchone()[0]

        # Insert line items
        for product_id in product_ids:
            cursor.execute(
                "INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, 10)",
                (order_id, product_id)
            )

        # Get results
        cursor.execute("""
            SELECT li.line_item_id, li.quantity, p.product_name
            FROM line_items li
            JOIN products p ON li.product_id = p.product_id
            WHERE li.order_id = ?
            ORDER BY li.line_item_id
        """, (order_id,))
        results = cursor.fetchall()

        print(f"\nTask 3: Order ID: {order_id}")
        for line_item_id, quantity, product_name in results:
            print(f"Line Item ID: {line_item_id}, Quantity: {quantity}, Product: {product_name}")

        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error in task3: {e}")
        if 'conn' in locals():
            conn.rollback()
    finally:
            conn.close()

def task4():
    try:
        conn = sqlite3.connect(r"C:\Users\lnpov\Documents\CTD_Project\python_class\python_homework\db\lesson.db")
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()
        query = """
        SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
        FROM employees e
        JOIN orders o ON e.employee_id = o.employee_id
        GROUP BY e.employee_id, e.first_name, e.last_name
        HAVING COUNT(o.order_id) > 5;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        print("\nTask 4: Employees with more than 5 orders")
        for emp_id, first_name, last_name, count in results:
            print(f"Employee ID: {emp_id}, Name: {first_name} {last_name}, Order Count: {count}")
    except sqlite3.Error as e:
        print(f"Database error in task4: {e}")
    finally:
            conn.close()

if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4()
