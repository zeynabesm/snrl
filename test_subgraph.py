from igeg.builder import IGEGBuilder
from igeg.edge import EdgeType

from igeg.path.extractor import EvidencePathExtractor
from igeg.path.scorer import EvidenceScorer
from igeg.reasoning.optimizer import EvidenceSubgraphOptimizer


# =====================================
# Build Graph
# =====================================

builder = IGEGBuilder()

intent = builder.add_intent({
    "name": "Predict Customer Churn",
    "task": "classification",
    "target": "churn",
    "entity": "customer"
})

concept = builder.add_concept("Customer")

customers = builder.add_table("Customers")
transactions = builder.add_table("Transactions")

amount = builder.add_attribute(
    "Transactions.amount",
    metadata={
        "datatype": "float"
    }
)

frequency = builder.add_attribute(
    "Transactions.frequency",
    metadata={
        "datatype": "int"
    }
)

late_payment = builder.add_attribute(
    "Transactions.late_payment",
    metadata={
        "datatype": "bool"
    }
)


# =====================================
# Intent → Concept → Table
# =====================================

builder.connect(intent, concept, EdgeType.SEMANTIC, weight=0.95)

builder.connect(concept, customers, EdgeType.MAPPING, weight=0.95)

builder.connect(
    customers,
    transactions,
    EdgeType.RELATIONAL,
    weight=1.0
)


builder.connect(
    transactions,
    amount,
    EdgeType.MAPPING,
    weight=0.95
)

builder.connect(
    transactions,
    frequency,
    EdgeType.MAPPING,
    weight=0.95
)

builder.connect(
    transactions,
    late_payment,
    EdgeType.MAPPING,
    weight=0.95
)

# =====================================
# Feature 1
# =====================================

avg = builder.add_operator("AVG")

feature1 = builder.add_feature(
    "AveragePurchaseValue"
)

builder.connect(
    amount,
    avg,
    EdgeType.FEATURE,
    weight=1.0
)

builder.connect(
    avg,
    feature1,
    EdgeType.FEATURE,
    weight=1.0
)

# =====================================
# Feature 2
# =====================================

count = builder.add_operator("COUNT")

feature2 = builder.add_feature(
    "PurchaseFrequency"
)

builder.connect(
    frequency,
    count,
    EdgeType.FEATURE,
    weight=0.92
)

builder.connect(
    count,
    feature2,
    EdgeType.FEATURE,
    weight=0.92
)

# =====================================
# Feature 3
# =====================================

sum_op = builder.add_operator("SUM")

feature3 = builder.add_feature(
    "LatePaymentScore"
)

builder.connect(
    late_payment,
    sum_op,
    EdgeType.FEATURE,
    weight=0.80
)

builder.connect(
    sum_op,
    feature3,
    EdgeType.FEATURE,
    weight=0.80
)

# =====================================
# Target
# =====================================

target = builder.add_target("Churn")

builder.connect(
    feature1,
    target,
    EdgeType.INFERENCE,
    weight=0.90
)

builder.connect(
    feature2,
    target,
    EdgeType.INFERENCE,
    weight=0.82
)

builder.connect(
    feature3,
    target,
    EdgeType.INFERENCE,
    weight=0.70
)

graph = builder.build()

# =====================================
# Extract Paths
# =====================================

extractor = EvidencePathExtractor(graph)

paths = extractor.extract_paths(
    intent.id,
    target.id
)

print("\nFOUND PATHS:", len(paths))

# =====================================
# Rank Subgraph
# =====================================

optimizer = EvidenceSubgraphOptimizer(
    EvidenceScorer()
)

subgraph = optimizer.optimize(paths)

print("\n========== BEST SUBGRAPH ==========\n")

print("Selected Paths :", len(subgraph.paths))
print("Nodes :", len(subgraph.nodes))
print("Edges :", len(subgraph.edges))
print("Score :", round(subgraph.score,3))

print("\n----- PATHS -----\n")

for i,path in enumerate(subgraph.paths,1):

    print("PATH",i)

    print(
        " -> ".join(
            node.name
            for node in path.nodes
        )
    )

    print(
        "Score:",
        round(path.score,3)
    )

    print()