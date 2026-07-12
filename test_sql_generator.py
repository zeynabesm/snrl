from test_feature_plan import plan

from igeg.planning.dataset_builder import DatasetPlanBuilder

from igeg.generation.sql_generator import SQLGenerator



# FeaturePlan -> DatasetPlan

builder = DatasetPlanBuilder()


dataset_plan = builder.build(

    plan

)



# DatasetPlan -> SQL


generator = SQLGenerator()


sql = generator.generate(

    dataset_plan

)



print("\n=== GENERATED SQL ===\n")


print(sql)