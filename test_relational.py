from igeg.schema import SchemaGraph

from igeg.relational_builder import RelationalBuilder

from igeg.builder import IGEGBuilder



builder = IGEGBuilder()


customers = builder.add_table(
    "Customers"
)


transactions = builder.add_table(
    "Transactions"
)



schema = SchemaGraph()



schema.add_relationship(

    "Customers",

    "Transactions",

    "customer_id",

    "customer_id"

)



rel_builder = RelationalBuilder(schema)



table_nodes = {

    "Customers": customers,

    "Transactions": transactions

}



rel_builder.build_edges(

    builder.graph,

    table_nodes

)



graph = builder.build()



graph.print_graph()


print(graph.to_dict())