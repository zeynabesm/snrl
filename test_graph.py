from igeg.graph import IGEGGraph

from igeg.node import IGEGNode, NodeType

from igeg.edge import IGEGEdge, EdgeType



graph = IGEGGraph()



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



graph.add_node(intent)

graph.add_node(concept)

graph.add_node(table)



edge1 = IGEGEdge(
    source=intent.id,
    target=concept.id,
    edge_type=EdgeType.SEMANTIC,
    weight=0.9
)


edge2 = IGEGEdge(
    source=concept.id,
    target=table.id,
    edge_type=EdgeType.MAPPING,
    weight=0.95
)



graph.add_edge(edge1)

graph.add_edge(edge2)



print(graph.to_dict())