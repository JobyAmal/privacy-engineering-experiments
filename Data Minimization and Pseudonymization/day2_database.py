import sqlite3

conn = sqlite3.connect("users.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customer_profiles
(
    user_id INTEGER PRIMARY KEY,
    full_name TEXT,
    email TEXT,
    ssn TEXT,
    state TEXT,
    purchase_amount REAL
);
""")

cursor.execute("DELETE FROM customer_profiles;")

cursor.executemany("""
INSERT INTO customer_profiles (full_name, email, ssn, state, purchase_amount)
VALUES (?, ?, ?, ?, ?);
""", [
    ("Alice Smith", "alice@example.com", "123-45-6789", "NY", 150.50),
    ("Bob Jones", "bob@example.com", "987-65-4321", "CA", 299.99),
    ("Charlie Brown", "charlie@example.com", "456-78-9012", "TX", 85.00)
    ])

conn.commit()
conn.close()

print ("Database successfully created and populated!")