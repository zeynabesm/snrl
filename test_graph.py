from igeg.graph import IGEGGraph
from igeg.node import IGEGNode, NodeType
from igeg.edge import IGEGEdge, EdgeType



graph = IGEGGraph()



# Nodes

intent = IGEGNode(
    NodeType.INTENT,
    "Predict Customer Churn"
)


customer = IGEGNode(
    NodeType.CONCEPT,
    "Customer"
)


table = IGEGNode(
    NodeType.TABLE,
    "Customers"
)



graph.add_node(intent)
graph.add_node(customer)
graph.add_node(table)



# Edges

e1 = IGEGEdge(

    source=intent.id,

    target=customer.id,

    edge_type=EdgeType.SEMANTIC,

    weight=0.9

)


e2 = IGEGEdge(

    source=customer.id,

    target=table.id,

    edge_type=EdgeType.MAPPING,

    weight=0.95

)



graph.add_edge(e1)
graph.add_edge(e2)



print("\nNeighbors of Intent:")

for n in graph.get_neighbors(intent.id):

    print(n)



print("\nOutgoing edges:")

for e in graph.get_outgoing_edges(customer.id):

    print(e)



print("\nIncoming edges of Customers:")

for e in graph.get_incoming_edges(table.id):

    print(e)



print("\nJSON:")

print(graph.to_dict())