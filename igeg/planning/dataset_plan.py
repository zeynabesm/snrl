class DatasetPlan:


    def __init__(self):

        self.entity_table = None

        self.joins = []

        self.features = []

        self.target = None



    def add_join(self, join):

        self.joins.append(join)



    def add_feature(self, feature):

        self.features.append(feature)



    def to_dict(self):

        return {

            "entity_table": self.entity_table,

            "joins": self.joins,

            "features": self.features,

            "target": self.target

        }



    def __repr__(self):

        return str(
            self.to_dict()
        )