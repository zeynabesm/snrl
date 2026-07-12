from dataclasses import dataclass, field


@dataclass
class EvidenceSubgraph:

    nodes: list = field(default_factory=list)

    edges: list = field(default_factory=list)

    paths: list = field(default_factory=list)

    score: float = 0.0


    def add_node(self, node):

        if node.id not in [n.id for n in self.nodes]:

            self.nodes.append(node)


    def add_edge(self, edge):

        if edge.id not in [e.id for e in self.edges]:

            self.edges.append(edge)


    def add_path(self, path):

        self.paths.append(path)


    @property
    def node_count(self):

        return len(self.nodes)


    @property
    def edge_count(self):

        return len(self.edges)


    @property
    def path_count(self):

        return len(self.paths)


    def to_dict(self):

        return {

            "score": self.score,

            "node_count": self.node_count,

            "edge_count": self.edge_count,

            "path_count": self.path_count,

            "nodes": [

                {

                    "id": n.id,

                    "type": n.node_type.value,

                    "name": n.name

                }

                for n in self.nodes

            ],

            "edges": [

                {

                    "source": e.source,

                    "target": e.target,

                    "type": e.edge_type.value,

                    "weight": e.weight

                }

                for e in self.edges

            ]

        }


    def __repr__(self):

        return (

            f"EvidenceSubgraph("

            f"nodes={self.node_count}, "

            f"edges={self.edge_count}, "

            f"paths={self.path_count}, "

            f"score={round(self.score,3)})"

        )