"""
IGEG Graph Engine

Core graph representation for SNRL.

Responsibilities:
- Store heterogeneous nodes
- Store typed edges
- Maintain adjacency indexes
- Support graph traversal
- Serialize graph structure
"""


class IGEGGraph:

    def __init__(self):

        # node_id -> Node
        self.nodes = {}

        # list of all edges
        self.edges = []

        # node_id -> list of outgoing edges
        self.adjacency = {}

        # node_id -> list of incoming edges
        self.incoming = {}

        # edge_id -> Edge
        self.edge_lookup = {}


    # -----------------------------
    # Node Management
    # -----------------------------

    def add_node(self, node):

        if node.id not in self.nodes:

            self.nodes[node.id] = node

            self.adjacency[node.id] = []

            self.incoming[node.id] = []

        return node



    def get_node(self, node_id):

        return self.nodes.get(node_id)



    # -----------------------------
    # Edge Management
    # -----------------------------

    def add_edge(self, edge):

        self.edges.append(edge)

        self.edge_lookup[edge.id] = edge


        # outgoing index

        if edge.source not in self.adjacency:
            self.adjacency[edge.source] = []

        self.adjacency[edge.source].append(edge)



        # incoming index

        if edge.target not in self.incoming:
            self.incoming[edge.target] = []

        self.incoming[edge.target].append(edge)



        return edge



    def get_edge(self, edge_id):

        return self.edge_lookup.get(edge_id)



    # -----------------------------
    # Traversal
    # -----------------------------

    def get_neighbors(self, node_id):

        neighbors = []

        for edge in self.adjacency.get(node_id, []):

            target_node = self.nodes.get(edge.target)

            if target_node:
                neighbors.append(target_node)

        return neighbors



    def get_outgoing_edges(self, node_id):

        return self.adjacency.get(node_id, [])



    def get_incoming_edges(self, node_id):

        return self.incoming.get(node_id, [])



    # -----------------------------
    # Serialization
    # -----------------------------

    def to_dict(self):

        return {

            "nodes":
                [
                    node.to_dict()
                    for node in self.nodes.values()
                ],

            "edges":
                [
                    edge.to_dict()
                    for edge in self.edges
                ]

        }