import sqlite3


connection = sqlite3.connect(
    "snrl.db"
)

cursor = connection.cursor()


# Customers table

cursor.execute(
"""
CREATE TABLE IF NOT EXISTS Customers
(
    customer_id INTEGER PRIMARY KEY,
    Churn INTEGER
)
"""
)



# Transactions table

cursor.execute(
"""
CREATE TABLE IF NOT EXISTS Transactions
(
    transaction_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount FLOAT
)
"""
)



# Insert customers

cursor.executemany(
"""
INSERT INTO Customers
(customer_id, Churn)
VALUES (?,?)
""",
[
    (1,0),
    (2,1),
    (3,0)
]
)



# Insert transactions

cursor.executemany(
"""
INSERT INTO Transactions
(customer_id, amount)
VALUES (?,?)
""",
[
    (1,100),
    (1,200),
    (2,50),
    (2,70),
    (3,300)
]
)



connection.commit()

connection.close()


print("Database created successfully")