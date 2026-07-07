from .edge import IGEGEdge, EdgeType



class RelationalBuilder:


    def __init__(self, schema_graph):

        self.schema_graph = schema_graph



    def build_edges(
        self,
        graph,
        table_nodes
    ):


        edges = []


        for relation in self.schema_graph.get_relationships():


            source = table_nodes.get(
                relation.source_table
            )

            target = table_nodes.get(
                relation.target_table
            )


            if source and target:


                edge = IGEGEdge(

                    source=source.id,

                    target=target.id,

                    edge_type=EdgeType.RELATIONAL,

                    weight=1.0,

                    metadata={

                        "source_column":
                            relation.source_column,

                        "target_column":
                            relation.target_column

                    }

                )


                graph.add_edge(edge)

                edges.append(edge)


        return edges