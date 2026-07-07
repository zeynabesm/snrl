from dataclasses import dataclass


@dataclass
class Relationship:

    source_table: str

    target_table: str

    source_column: str

    target_column: str



class SchemaGraph:


    def __init__(self):

        self.relationships = []



    def add_relationship(
        self,
        source_table,
        target_table,
        source_column,
        target_column
    ):

        relation = Relationship(
            source_table,
            target_table,
            source_column,
            target_column
        )

        self.relationships.append(relation)



    def get_relationships(self):

        return self.relationships