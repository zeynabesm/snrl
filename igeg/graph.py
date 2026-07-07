from typing import Dict, List

from .node import IGEGNode
from .edge import IGEGEdge


class IGEGGraph:

    def __init__(self):

        self.nodes: Dict[str, IGEGNode] = {}

        self.edges: List[IGEGEdge] = []


    def add_node(self, node: IGEGNode):

        self.nodes[node.id] = node

        return node.id


    def add_edge(self, edge: IGEGEdge):

        self.edges.append(edge)


    def get_node(self, node_id):

        return self.nodes.get(node_id)


    def get_neighbors(self, node_id):

        neighbors = []

        for edge in self.edges:

            if edge.source == node_id:

                neighbors.append(
                    self.nodes[edge.target]
                )

        return neighbors


    def to_dict(self):

        return {

            "nodes": [

                node.to_dict()

                for node in self.nodes.values()

            ],

            "edges": [

                edge.to_dict()

                for edge in self.edges

            ]

        }