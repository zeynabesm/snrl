from igeg.builder import IGEGBuilder
from igeg.feature_builder import FeatureBuilder
from igeg.edge import EdgeType



builder = IGEGBuilder()


table = builder.add_table(
    "Transactions"
)


amount = builder.add_attribute(
    "amount"
)



feature_builder = FeatureBuilder(
    builder.get_graph()
)



feature = feature_builder.create_feature(

    attribute=amount,

    operator="AVG",

    feature_name="AveragePurchaseValue",

    metadata={

        "source":"Transactions.amount",

        "purpose":"churn prediction"

    }

)



graph = builder.build()



print("\n=== Feature Node ===")

print(feature)



print("\n=== Graph JSON ===")

print(graph.to_dict())