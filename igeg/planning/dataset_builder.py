from igeg.planning.dataset_plan import DatasetPlan



class DatasetPlanBuilder:


    def __init__(self):

        pass



    def build(
        self,
        feature_plan
    ):


        dataset_plan = DatasetPlan()



        # Entity

        dataset_plan.entity_table = (
            feature_plan.entity
        )



        # Target

        dataset_plan.target = (
            feature_plan.target
        )



        # Features

        for feature in feature_plan.features:


            dataset_plan.add_feature(

                {

                    "name":
                        feature["name"],


                    "expression":
                        f"{feature['operator']}("
                        f"{feature['source']}"
                        f")",


                    "source":
                        feature["source"]

                }

            )



        # Joins

        for join in feature_plan.join_path:


            dataset_plan.add_join(

                {

                    "left":
                        f"{join['source_table']}."
                        f"{join['source_column']}",


                    "right":
                        f"{join['target_table']}."
                        f"{join['target_column']}",


                    "type":
                        join["type"]

                }

            )



        return dataset_plan