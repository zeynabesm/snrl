from igeg.graph import IGEGGraph
from igeg.builder import IGEGBuilder
from igeg.reasoning.path_builder import EvidencePathExtractor
from igeg.node import IGEGNode
from igeg.edge import IGEGEdge

from igeg.builder import IGEGBuilder
from igeg.edge import EdgeType



builder = IGEGBuilder()



intent = builder.add_intent(
    {
        "name":"Predict Customer Churn",
        "task":"classification",
        "target":"churn",
        "entity":"customer"
    }
)


concept = builder.add_concept(
    "Customer"
)


customers = builder.add_table(
    "Customers"
)


transactions = builder.add_table(
    "Transactions"
)



amount = builder.add_attribute(
    "Transactions.amount"
)



operator = builder.add_operator(
    "AVG"
)



feature = builder.add_feature(
    "AveragePurchaseValue",
    {
        "source":"Transactions.amount",
        "purpose":"churn prediction"
    }
)



target = builder.add_target(
    "Churn",
    {
        "task":"classification",
        "type":"binary"
    }
)



builder.connect(
    intent,
    concept,
    EdgeType.SEMANTIC,
    0.9
)



builder.connect(
    concept,
    customers,
    EdgeType.MAPPING,
    0.95
)



builder.connect(
    customers,
    transactions,
    EdgeType.RELATIONAL,
    1.0
)



builder.connect(
    amount,
    operator,
    EdgeType.FEATURE,
    1.0
)



builder.connect(
    operator,
    feature,
    EdgeType.FEATURE,
    1.0
)



builder.connect(
    feature,
    target,
    EdgeType.INFERENCE,
    0.85
)



graph = builder.build()



extractor = EvidencePathExtractor(graph)



path = extractor.find_path(
    intent,
    target
)



extractor.print_path(path)