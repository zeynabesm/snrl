class JoinResolver:


    def __init__(self, alias_manager):

        self.alias_manager = alias_manager



    def resolve(self, join):


        left_table = (
            join["left"].split(".")[0]
        )

        right_table = (
            join["right"].split(".")[0]
        )


        left_column = (
            join["left"].split(".")[1]
        )

        right_column = (
            join["right"].split(".")[1]
        )


        left_alias = (
            self.alias_manager.get_alias(
                left_table
            )
        )


        right_alias = (
            self.alias_manager.get_alias(
                right_table
            )
        )


        return {

            "table":
                right_table,


            "alias":
                right_alias,


            "condition":
                f"{left_alias}.{left_column} "
                f"= "
                f"{right_alias}.{right_column}"

        }