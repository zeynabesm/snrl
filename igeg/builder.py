from .graph import IGEGGraph
from .node import IGEGNode, NodeType
from .edge import IGEGEdge, EdgeType



class IGEGBuilder:


    def __init__(self):

        self.graph = IGEGGraph()



    # =========================
    # Node Creation
    # =========================


    def add_intent(
        self,
        intent_data
    ):

        node = IGEGNode(

            node_type=NodeType.INTENT,

            name=intent_data["name"],

            metadata=intent_data

        )


        self.graph.add_node(node)


        return node




    def add_concept(
        self,
        concept_name,
        metadata=None
    ):

        node = IGEGNode(

            node_type=NodeType.CONCEPT,

            name=concept_name,

            metadata=metadata or {}

        )


        self.graph.add_node(node)


        return node





    def add_table(
        self,
        table_name,
        metadata=None
    ):

        node = IGEGNode(

            node_type=NodeType.TABLE,

            name=table_name,

            metadata=metadata or {}

        )


        self.graph.add_node(node)


        return node





    def add_attribute(
        self,
        attribute_name,
        metadata=None
    ):

        node = IGEGNode(

            node_type=NodeType.ATTRIBUTE,

            name=attribute_name,

            metadata=metadata or {}

        )


        self.graph.add_node(node)


        return node





    def add_operator(
        self,
        operator_name,
        metadata=None
    ):

        node = IGEGNode(

            node_type=NodeType.OPERATOR,

            name=operator_name,

            metadata=metadata or {}

        )


        self.graph.add_node(node)


        return node





    def add_feature(
        self,
        feature_name,
        metadata=None
    ):

        node = IGEGNode(

            node_type=NodeType.FEATURE,

            name=feature_name,

            metadata=metadata or {}

        )


        self.graph.add_node(node)


        return node





    def add_target(
        self,
        target_name,
        metadata=None
    ):

        node = IGEGNode(

            node_type=NodeType.TARGET,

            name=target_name,

            metadata=metadata or {}

        )


        self.graph.add_node(node)


        return node





    # =========================
    # Edge Creation
    # =========================


    def connect(
        self,
        source,
        target,
        edge_type,
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





    # =========================
    # Build
    # =========================


    def build(self):

        return self.graph