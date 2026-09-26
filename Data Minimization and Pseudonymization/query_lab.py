import sqlite3

conn = sqlite3.connect ("users.db")
cursor = conn.cursor()

print ("**** Pseudonymized Query (Masked Identifiers) ****")

cursor.execute("""
SELECT
    SUBSTR(email, 1, 1) || "***@" || SUBSTR(email, INSTR(email, '@') + 1) AS masked_email,
    state,
    purchase_amount
FROM customer_profiles;
""")

rows = cursor.fetchall()

for row in rows:
    print (row)

conn.close()