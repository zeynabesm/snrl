from igeg.planning.feature_plan import FeaturePlan
from igeg.planning.join_extractor import JoinPathExtractor



class FeaturePlanner:


    def __init__(self):

        self.join_extractor = JoinPathExtractor()



    def build_plan(
        self,
        subgraph
    ):


        plan = FeaturePlan()



        if isinstance(subgraph.nodes, dict):

            nodes = subgraph.nodes.values()

        else:

            nodes = subgraph.nodes



        # =========================
        # Nodes
        # =========================

        for node in nodes:


            node_type = node.node_type.value



            if node_type == "target":


                plan.target = node.name



            elif node_type == "table":


                if plan.entity is None:

                    plan.entity = node.name



            elif node_type == "feature":


                metadata = node.metadata



                plan.add_feature(

                    name=node.name,


                    source=
                    f"{metadata.get('source_table')}"
                    f"."
                    f"{metadata.get('source_column')}",


                    operator=
                    metadata.get(
                        "aggregation"
                    ),


                    metadata=metadata

                )



            plan.add_trace(

                f"{node_type}: {node.name}"

            )



        # =========================
        # Join Extraction
        # =========================

        joins = self.join_extractor.extract(
            subgraph
        )



        for join in joins:


            plan.join_path.append(
                join
            )



        return plan