from igeg.path.scorer import EvidenceScorer


class EvidenceSubgraph:

    def __init__(self, paths):

        self.paths = paths

        self.nodes = []
        self.edges = []

        self.score = 0.0


class EvidenceSubgraphOptimizer:

    def __init__(self, scorer=None):

        self.scorer = scorer or EvidenceScorer()

    def optimize(self, paths):

        for p in paths:
            p.score = self.scorer.score(p)

        ranked = sorted(
            paths,
            key=lambda x: x.score,
            reverse=True
        )

        selected = ranked[:2]

        subgraph = EvidenceSubgraph(selected)

        node_ids = set()
        edge_ids = set()

        for path in selected:

            for node in path.nodes:

                if node.id not in node_ids:

                    node_ids.add(node.id)
                    subgraph.nodes.append(node)

            for edge in path.edges:

                if edge.id not in edge_ids:

                    edge_ids.add(edge.id)
                    subgraph.edges.append(edge)

        if selected:

            subgraph.score = sum(
                p.score for p in selected
            ) / len(selected)

        return subgraph