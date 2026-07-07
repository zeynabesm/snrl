from igeg.builder import IGEGBuilder
from igeg.node import IGEGNode, NodeType


builder = IGEGBuilder()


attribute = IGEGNode(
    NodeType.ATTRIBUTE,
    "Transactions.amount"
)


builder.add_node(attribute)



builder.add_feature_path(
    attribute_node=attribute,
    operator="AVG",
    feature_name="Average Purchase Value",
    target_name="Churn"
)



graph = builder.build()


print(graph.to_dict())