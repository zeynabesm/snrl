from igeg.edge import EdgeType



class JoinPathExtractor:


    def __init__(self):
        pass



    def extract(
        self,
        graph
    ):


        joins = []



        for edge in graph.edges:


            if edge.edge_type == EdgeType.RELATIONAL:



                source_node = graph.nodes[
                    edge.source
                ]


                target_node = graph.nodes[
                    edge.target
                ]



                metadata = edge.metadata



                joins.append(

                    {

                        "source_table":
                            source_node.name,


                        "source_column":
                            metadata.get(
                                "source_column"
                            ),


                        "target_table":
                            target_node.name,


                        "target_column":
                            metadata.get(
                                "target_column"
                            ),


                        "type":
                            "inner_join"

                    }

                )



        return joins