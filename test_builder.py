from igeg.builder import IGEGBuilder
from igeg.node import IGEGNode, NodeType
from igeg.edge import EdgeType


builder = IGEGBuilder()


intent = IGEGNode(
    NodeType.INTENT,
    "Predict Customer Churn"
)


concept = IGEGNode(
    NodeType.CONCEPT,
    "Customer"
)


table = IGEGNode(
    NodeType.TABLE,
    "Customers"
)


builder.add_node(intent)
builder.add_node(concept)
builder.add_node(table)


builder.connect(
    intent,
    concept,
    EdgeType.SEMANTIC,
    weight=0.9,
    metadata={
        "reason": "intent understanding"
    }
)


builder.connect(
    concept,
    table,
    EdgeType.MAPPING,
    weight=0.95,
    metadata={
        "reason": "schema grounding"
    }
)


igeg = builder.build()


print(igeg.to_dict())