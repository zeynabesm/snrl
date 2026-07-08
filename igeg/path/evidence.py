class EvidencePath:


    def __init__(
        self,
        nodes,
        edges
    ):

        self.nodes = nodes
        self.edges = edges
        self.score = None



    def node_names(self):

        return [
            node.name
            for node in self.nodes
        ]



    def edge_types(self):

        return [
            edge.edge_type.value
            for edge in self.edges
        ]



    def calculate_length(self):

        return len(self.edges)



    def set_score(
        self,
        score
    ):

        self.score = score



    def to_dict(self):

        return {

            "nodes":
            [
                node.to_dict()
                for node in self.nodes
            ],


            "edges":
            [
                edge.to_dict()
                for edge in self.edges
            ],


            "score":
            self.score
        }



    def explain(self):

        result = []


        for i, edge in enumerate(self.edges):

            result.append(
                {
                    "from":
                    self.nodes[i].name,

                    "to":
                    self.nodes[i+1].name,

                    "relation":
                    edge.edge_type.value,

                    "weight":
                    edge.weight
                }
            )


        return result



    def __repr__(self):

        path = " → ".join(
            self.node_names()
        )


        if self.score:

            return (
                f"{path}\n"
                f"Score={self.score}"
            )


        return path