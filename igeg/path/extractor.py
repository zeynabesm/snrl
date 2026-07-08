from collections import deque

from igeg.path.evidence import EvidencePath



class EvidencePathExtractor:


    def __init__(self, graph):

        self.graph = graph



    def extract_paths(
        self,
        start,
        end,
        max_depth=10
    ):


        paths = []


        queue = deque()


        queue.append(
            (
                start,
                [start],
                []
            )
        )



        while queue:


            current, nodes, edges = queue.popleft()



            if current == end:


                paths.append(

                    self._create_path(
                        nodes,
                        edges
                    )

                )

                continue



            if len(nodes) >= max_depth:
                continue



            for edge in self.graph.edges:


                if edge.source == current:


                    if edge.target not in nodes:


                        queue.append(
                            (
                                edge.target,
                                nodes + [edge.target],
                                edges + [edge]
                            )
                        )



        return paths



    # compatibility

    def extract(
        self,
        start,
        end,
        max_depth=10
    ):

        return self.extract_paths(
            start,
            end,
            max_depth
        )



    def _create_path(
        self,
        node_ids,
        edges
    ):


        nodes = [

            self.graph.nodes[node_id]

            for node_id in node_ids

        ]


        return EvidencePath(
            nodes,
            edges
        )