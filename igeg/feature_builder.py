from .node import IGEGNode, NodeType
from .edge import IGEGEdge, EdgeType


class FeatureBuilder:


    def __init__(self, graph):

        self.graph = graph



    def create_feature(
            self,
            attribute,
            operator,
            feature_name,
            metadata=None
    ):

        # Operator Node

        operator_node = IGEGNode(

            node_type=NodeType.OPERATOR,

            name=operator

        )


        self.graph.add_node(operator_node)



        # Feature Node

        feature_node = IGEGNode(

            node_type=NodeType.FEATURE,

            name=feature_name,

            metadata=metadata or {}

        )


        self.graph.add_node(feature_node)



        # Attribute -> Operator

        edge1 = IGEGEdge(

            source=attribute.id,

            target=operator_node.id,

            edge_type=EdgeType.FEATURE,

            weight=1.0,

            metadata={

                "operation": operator

            }

        )


        self.graph.add_edge(edge1)



        # Operator -> Feature

        edge2 = IGEGEdge(

            source=operator_node.id,

            target=feature_node.id,

            edge_type=EdgeType.FEATURE,

            weight=1.0,

            metadata={

                "generated_feature": feature_name

            }

        )


        self.graph.add_edge(edge2)



        return feature_node





    def create_target(

            self,

            target_name,

            metadata=None

    ):


        target_node = IGEGNode(

            node_type=NodeType.TARGET,

            name=target_name,

            metadata=metadata or {}

        )


        self.graph.add_node(target_node)


        return target_node





    def connect_feature_to_target(

            self,

            feature,

            target,

            weight=1.0,

            metadata=None

    ):


        inference_edge = IGEGEdge(

            source=feature.id,

            target=target.id,

            edge_type=EdgeType.INFERENCE,

            weight=weight,

            metadata=metadata or {}

        )


        self.graph.add_edge(inference_edge)


        return inference_edge