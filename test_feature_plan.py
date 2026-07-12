from igeg.planning.planner import FeaturePlanner

from igeg.builder import IGEGBuilder
from igeg.edge import EdgeType



# =====================================================
# Build Evidence Subgraph Example
# =====================================================

builder = IGEGBuilder()



# =====================================================
# Intent
# =====================================================

intent = builder.add_intent(

    {
        "name": "Predict Customer Churn",
        "task": "classification",
        "target": "churn",
        "entity": "customer"
    }

)



# =====================================================
# Tables
# =====================================================

customer_table = builder.add_table(
    "Customers"
)



transaction_table = builder.add_table(
    "Transactions"
)



# =====================================================
# Relational Edge
# =====================================================

builder.connect(

    customer_table,

    transaction_table,

    EdgeType.RELATIONAL,

    weight=1.0,

    metadata={

        "source_column": "customer_id",

        "target_column": "customer_id"

    }

)



# =====================================================
# Feature
# =====================================================

feature = builder.add_feature(

    "AveragePurchaseValue",

    metadata={

        "source_table": "Transactions",

        "source_column": "amount",

        "aggregation": "AVG",

        "window": "30_days",

        "business_meaning":
            "average customer spending"

    }

)



builder.connect(

    transaction_table,

    feature,

    EdgeType.FEATURE,

    weight=1.0,

    metadata={

        "operation": "AVG"

    }

)



# =====================================================
# Target
# =====================================================

target = builder.add_target(

    "Churn",

    metadata={

        "task": "classification",

        "type": "binary"

    }

)



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



# =====================================================
# Build Graph
# =====================================================

graph = builder.build()



# =====================================================
# Feature Planning
# =====================================================

planner = FeaturePlanner()



plan = planner.build_plan(

    graph

)



print("\n=== FEATURE PLAN ===\n")


print(

    plan.to_dict()

)



# =====================================================
# Join Path
# =====================================================

print("\n=== JOIN PATH ===\n")


for join in plan.join_path:

    print(join)