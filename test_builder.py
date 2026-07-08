from igeg.builder import IGEGBuilder
from igeg.edge import EdgeType



builder = IGEGBuilder()



intent = builder.add_intent({

    "name":"Predict Customer Churn",

    "task":"classification",

    "target":"churn",

    "entity":"customer"

})



concept = builder.add_concept(
    "Customer"
)


table = builder.add_table(
    "Customers"
)


attribute = builder.add_attribute(
    "customer_id"
)


builder.connect(

    intent,

    concept,

    EdgeType.SEMANTIC,

    0.9,

    {
        "reason":"intent understanding"
    }

)


builder.connect(

    concept,

    table,

    EdgeType.MAPPING,

    0.95,

    {
        "reason":"schema grounding"
    }

)


builder.connect(

    table,

    attribute,

    EdgeType.RELATIONAL,

    1.0

)



graph = builder.build()



print(graph.to_dict())