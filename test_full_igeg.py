from igeg.builder import IGEGBuilder
from igeg.edge import EdgeType
import json


builder = IGEGBuilder()


# ==================================================
# Intent
# ==================================================

intent = builder.add_intent(
    {
        "name": "Predict Customer Churn",
        "task": "classification",
        "target": "churn",
        "entity": "customer"
    }
)


# ==================================================
# Concept
# ==================================================

customer_concept = builder.add_concept(
    "Customer"
)


# ==================================================
# Tables
# ==================================================

customers_table = builder.add_table(
    "Customers"
)


transactions_table = builder.add_table(
    "Transactions"
)


# ==================================================
# Attribute
# ==================================================

amount_attribute = builder.add_attribute(
    "Transactions.amount",
    metadata={
        "table": "Transactions",
        "column": "amount",
        "datatype": "float",
        "semantic": "purchase amount"
    }
)


# ==================================================
# Semantic Relation
# ==================================================

builder.connect(
    intent,
    customer_concept,
    EdgeType.SEMANTIC,
    weight=0.9,
    metadata={
        "reason": "intent understanding"
    }
)


# ==================================================
# Schema Grounding
# ==================================================

builder.connect(
    customer_concept,
    customers_table,
    EdgeType.MAPPING,
    weight=0.95,
    metadata={
        "reason": "schema grounding"
    }
)


# ==================================================
# Relational Path
# ==================================================

builder.connect(
    customers_table,
    transactions_table,
    EdgeType.RELATIONAL,
    weight=1.0,
    metadata={
        "source_column": "customer_id",
        "target_column": "customer_id"
    }
)


# ==================================================
# Table -> Attribute Mapping
# ==================================================

builder.connect(
    transactions_table,
    amount_attribute,
    EdgeType.MAPPING,
    weight=0.95,
    metadata={
        "reason": "attribute belongs to table"
    }
)



# ==================================================
# Feature Construction
# ==================================================

operator = builder.add_operator(
    "AVG"
)


feature = builder.add_feature(
    "AveragePurchaseValue",
    metadata={

        "source_table": "Transactions",

        "source_column": "amount",

        "aggregation": "AVG",

        "window": "30_days",

        "business_meaning":
            "average customer spending",

        "task":
            "classification"
    }
)



builder.connect(
    amount_attribute,
    operator,
    EdgeType.FEATURE,
    weight=1.0,
    metadata={
        "operation":"AVG"
    }
)



builder.connect(
    operator,
    feature,
    EdgeType.FEATURE,
    weight=1.0,
    metadata={
        "generated_feature":
            "AveragePurchaseValue"
    }
)



# ==================================================
# Target
# ==================================================

target = builder.add_target(
    "Churn",
    metadata={
        "task":"classification",
        "type":"binary"
    }
)



# ==================================================
# Inference Relation
# ==================================================

builder.connect(
    feature,
    target,
    EdgeType.INFERENCE,
    weight=0.85,
    metadata={
        "reason":
        "feature contributes to churn prediction"
    }
)



# ==================================================
# Build Graph
# ==================================================

graph = builder.build()



# ==================================================
# Export JSON
# ==================================================

with open(
    "mv_igeg.json",
    "w"
) as f:

    json.dump(
        graph.to_dict(),
        f,
        indent=4
    )



# ==================================================
# Print Graph
# ==================================================

print("\n=== FULL MV-IGEG ===\n")

print(graph.to_dict())



print("\n=== EDGES ===\n")


for e in graph.edges:

    source = graph.nodes[e.source].name
    target_name = graph.nodes[e.target].name


    print(
        f"{source} --[{e.edge_type.value}]--> {target_name}"
    )



# ==================================================
# Evidence Path Visualization
# ==================================================

print("\n=== EVIDENCE PATH ===\n")


path = [

    intent.name,

    customer_concept.name,

    customers_table.name,

    transactions_table.name,

    amount_attribute.name,

    operator.name,

    feature.name,

    target.name

]


print(
    "\n ↓ \n".join(path)
)



# ==================================================
# Validation
# ==================================================

print("\n=== VALIDATION ===\n")


node_types = [
    n.node_type.value
    for n in graph.nodes.values()
]


checks = {

    "Intent":
        "intent" in node_types,

    "Schema grounding":
        "table" in node_types,

    "Feature generation":
        "feature" in node_types,

    "Target inference":
        "target" in node_types

}


for k,v in checks.items():

    print(
        k,
        ":",
        "OK" if v else "FAILED"
    )