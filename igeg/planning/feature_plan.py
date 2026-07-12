class FeaturePlan:


    def __init__(
        self,
        target=None,
        entity=None
    ):

        self.target = target

        self.entity = entity

        self.features = []

        self.join_path = []

        self.reasoning_trace = []



    def add_feature(
        self,
        name,
        source,
        operator,
        metadata=None
    ):

        self.features.append(

            {
                "name": name,
                "source": source,
                "operator": operator,
                "metadata": metadata or {}
            }

        )



    def add_join(
        self,
        source,
        target,
        key
    ):

        self.join_path.append(

            {
                "source": source,
                "target": target,
                "key": key
            }

        )



    def add_trace(
        self,
        message
    ):

        self.reasoning_trace.append(
            message
        )



    def to_dict(self):

        return {

            "target": self.target,

            "entity": self.entity,

            "features": self.features,

            "join_path": self.join_path,

            "reasoning_trace": self.reasoning_trace

        }



    def __repr__(self):

        return str(
            self.to_dict()
        )