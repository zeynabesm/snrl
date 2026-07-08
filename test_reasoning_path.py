from igeg.builder import IGEGBuilder
from igeg.edge import EdgeType

from igeg.path.extractor import EvidencePathExtractor
from igeg.path.scorer import EvidenceScorer



# =====================================================
# Build Graph
# =====================================================

builder = IGEGBuilder()



# ---------------------
# Intent
# ---------------------

intent = builder.add_intent(
    {
        "name": "Predict Customer Churn",
        "task": "classification",
        "target": "churn",
        "entity": "customer"
    }
)



# ---------------------
# Concept
# ---------------------

customer = builder.add_concept(
    "Customer"
)



# ---------------------
# Tables
# ---------------------

customers = builder.add_table(
    "Customers"
)


transactions = builder.add_table(
    "Transactions"
)



# ---------------------
# Attribute
# ---------------------

amount = builder.add_attribute(
    "Transactions.amount",
    metadata={
        "table": "Transactions",
        "column": "amount",
        "datatype": "float",
        "semantic": "purchase amount"
    }
)



# ---------------------
# Semantic
# ---------------------

builder.connect(
    intent,
    customer,
    EdgeType.SEMANTIC,
    weight=0.9
)



# ---------------------
# Mapping
# ---------------------

builder.connect(
    customer,
    customers,
    EdgeType.MAPPING,
    weight=0.95
)



# ---------------------
# Relation
# ---------------------

builder.connect(
    customers,
    transactions,
    EdgeType.RELATIONAL,
    weight=1.0,
    metadata={
        "source_column":"customer_id",
        "target_column":"customer_id"
    }
)



# ---------------------
# Attribute mapping
# ---------------------

builder.connect(
    transactions,
    amount,
    EdgeType.MAPPING,
    weight=0.95
)



# ---------------------
# Feature
# ---------------------

operator = builder.add_operator(
    "AVG"
)


feature = builder.add_feature(
    "AveragePurchaseValue",
    metadata={
        "source":"Transactions.amount",
        "aggregation":"AVG",
        "window":"30_days"
    }
)



builder.connect(
    amount,
    operator,
    EdgeType.FEATURE,
    metadata={
        "operation":"AVG"
    }
)



builder.connect(
    operator,
    feature,
    EdgeType.FEATURE,
    metadata={
        "generated_feature":"AveragePurchaseValue"
    }
)



# ---------------------
# Target
# ---------------------

target = builder.add_target(
    "Churn",
    metadata={
        "task":"classification",
        "type":"binary"
    }
)



# ---------------------
# Inference
# ---------------------

builder.connect(
    feature,
    target,
    EdgeType.INFERENCE,
    weight=0.85,
    metadata={
        "reason":"feature contributes to churn prediction"
    }
)



graph = builder.build()



# =====================================================
# Print Edges
# =====================================================

print("\n=== EDGES ===")

for e in graph.edges:

    print(
        f"{graph.nodes[e.source].name} "
        f"--[{e.edge_type.value}]--> "
        f"{graph.nodes[e.target].name}"
    )



# =====================================================
# Extract Evidence Path
# =====================================================

extractor = EvidencePathExtractor(
    graph
)



paths = extractor.extract_paths(
    start=intent.id,
    end=target.id
)



print("\n=== REASONING PATHS ===")



scorer = EvidenceScorer()



for path in paths:


    print("\nPATH:")


    print(
        " → ".join(
            node.name
            for node in path.nodes
        )
    )



    print("\nEDGE TRACE:")


    for edge in path.edges:

        print(
            {
                "from":
                    graph.nodes[edge.source].name,

                "to":
                    graph.nodes[edge.target].name,

                "relation":
                    edge.edge_type.value,

                "weight":
                    edge.weight
            }
        )



    print("\n=== SCORE ===")


    score = scorer.score(path)

    print(
        "FINAL SCORE:",
        score
    )



    print("\nBREAKDOWN:")


    for k,v in scorer.breakdown(path).items():

        print(
            k,
            ":",
            v
        )