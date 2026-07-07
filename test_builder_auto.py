from igeg.builder import IGEGBuilder


builder = IGEGBuilder()


grounding = {

    "Customer": {

        "table": "Customers",
        "attribute": "customer_id"

    },

    "Purchase": {

        "table": "Transactions",
        "attribute": "amount"

    }

}


graph = builder.build_from_grounding(
    "Predict Customer Churn",
    grounding
)


print(graph.to_dict())