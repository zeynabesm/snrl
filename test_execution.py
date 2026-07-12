from igeg.execution.database import SQLiteDatabase
from igeg.execution.executor import DatasetExecutor



db = SQLiteDatabase(
    "snrl.db"
)



executor = DatasetExecutor(
    db
)



sql = """

SELECT
    c.customer_id,
    AVG(t.amount) AS AveragePurchaseValue,
    c.Churn

FROM Customers c

JOIN Transactions t

ON c.customer_id=t.customer_id

GROUP BY
    c.customer_id;

"""



dataset = executor.run(sql)



print("\n=== DATASET ===\n")

print(dataset)



X,y = executor.split_target(
    dataset,
    "Churn"
)



print("\n=== FEATURES ===")

print(X)



print("\n=== TARGET ===")

print(y)