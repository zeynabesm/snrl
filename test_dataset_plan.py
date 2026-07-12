from igeg.planning.dataset_builder import DatasetPlanBuilder

from test_feature_plan import plan



builder = DatasetPlanBuilder()



dataset_plan = builder.build(

    plan

)



print("\n=== DATASET PLAN ===\n")


print(

    dataset_plan.to_dict()

)