from enum import Enum
import uuid



class NodeType(Enum):

    INTENT = "intent"

    CONCEPT = "concept"

    TABLE = "table"

    ATTRIBUTE = "attribute"

    OPERATOR = "operator"

    FEATURE = "feature"

    TARGET = "target"




class IGEGNode:


    def __init__(
        self,
        node_type,
        name,
        metadata=None
    ):


        self.id = str(uuid.uuid4())

        self.node_type = node_type

        self.name = name

        self.metadata = metadata or {}



    def to_dict(self):

        return {

            "id": self.id,

            "type": self.node_type.value,

            "name": self.name,

            "metadata": self.metadata

        }




    def __repr__(self):

        return (
            f"IGEGNode("
            f"node_type={self.node_type}, "
            f"name='{self.name}', "
            f"id='{self.id}', "
            f"metadata={self.metadata}"
            f")"
        )