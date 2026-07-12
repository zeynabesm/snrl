from igeg.generation.alias_manager import AliasManager

from igeg.generation.join_resolver import JoinResolver

from igeg.generation.feature_compiler import FeatureExpressionCompiler




class SQLGenerator:



    def __init__(self):

        self.alias_manager = AliasManager()

        self.join_resolver = JoinResolver(

            self.alias_manager

        )

        self.feature_compiler = FeatureExpressionCompiler()



    def generate(self, dataset_plan):


        entity = dataset_plan.entity_table


        entity_alias = (

            self.alias_manager.get_alias(
                entity
            )

        )


        select_parts = []

        group_by = []



        # Entity key

        select_parts.append(

            f"{entity_alias}.customer_id"

        )


        group_by.append(

            f"{entity_alias}.customer_id"

        )



        # Features

        for feature in dataset_plan.features:


            compiled = (

                self.feature_compiler.compile(
                    feature
                )

            )


            select_parts.append(

                f"{compiled['expression']} "
                f"AS {compiled['name']}"

            )



        # Target

        if dataset_plan.target:


            select_parts.append(

                f"{entity_alias}.{dataset_plan.target}"

            )



        sql = (

            "SELECT\n    "

            +

            ",\n    ".join(select_parts)

            +

            f"\n\nFROM {entity} {entity_alias}"

        )



        # Joins

        for join in dataset_plan.joins:


            resolved = (

                self.join_resolver.resolve(
                    join
                )

            )


            sql += (

                f"\n\nJOIN "
                f"{resolved['table']} "
                f"{resolved['alias']}"

                f"\nON "
                f"{resolved['condition']}"

            )



        sql += (

            "\n\nGROUP BY\n    "

            +

            ",\n    ".join(group_by)

        )



        return sql + ";"