from .graph import IGEGGraph
from .node import IGEGNode, NodeType
from .edge import IGEGEdge, EdgeType


class IGEGBuilder:

    def __init__(self):
        self.graph = IGEGGraph()


    def add_node(self, node: IGEGNode):

        self.graph.add_node(node)

        return node


    def connect(
        self,
        source: IGEGNode,
        target: IGEGNode,
        edge_type: EdgeType,
        weight=1.0,
        metadata=None
    ):

        edge = IGEGEdge(
            source=source.id,
            target=target.id,
            edge_type=edge_type,
            weight=weight,
            metadata=metadata or {}
        )

        self.graph.add_edge(edge)

        return edge


    def build(self):

        return self.graph


    def build_from_grounding(
        self,
        intent,
        grounding
    ):

        intent_node = IGEGNode(
            NodeType.INTENT,
            intent
        )

        self.add_node(intent_node)


        for concept, schema in grounding.items():

            concept_node = IGEGNode(
                NodeType.CONCEPT,
                concept
            )

            self.add_node(concept_node)


            self.connect(
                intent_node,
                concept_node,
                EdgeType.SEMANTIC,
                weight=0.9,
                metadata={
                    "reason": "intent concept relation"
                }
            )


            table_node = IGEGNode(
                NodeType.TABLE,
                schema["table"]
            )

            self.add_node(table_node)


            self.connect(
                concept_node,
                table_node,
                EdgeType.MAPPING,
                weight=0.95,
                metadata={
                    "reason": "schema grounding"
                }
            )


            if "attribute" in schema:

                attribute_node = IGEGNode(
                    NodeType.ATTRIBUTE,
                    schema["attribute"]
                )

                self.add_node(attribute_node)


                self.connect(
                    table_node,
                    attribute_node,
                    EdgeType.RELATIONAL,
                    weight=1.0,
                    metadata={
                        "reason": "schema relationship"
                    }
                )


        return self.graph