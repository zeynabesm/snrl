from igeg.builder import IGEGBuilder
from igeg.edge import EdgeType

from igeg.path.extractor import EvidencePathExtractor
from igeg.path.scorer import EvidenceScorer

from igeg.reasoning.path_ranker import EvidencePathRanker
from igeg.reasoning.selector import TopKSelector



builder = IGEGBuilder()



# Intent

intent = builder.add_intent(
{
"name":"Predict Customer Churn",
"task":"classification",
"target":"churn"
}
)



customer = builder.add_concept(
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
"AveragePurchaseValue"
)



target = builder.add_target(
"Churn"
)



# edges


builder.connect(
intent,
customer,
EdgeType.SEMANTIC,
weight=.9
)



builder.connect(
customer,
customers,
EdgeType.MAPPING,
weight=.95
)



builder.connect(
customers,
transactions,
EdgeType.RELATIONAL,
weight=1
)



builder.connect(
transactions,
amount,
EdgeType.MAPPING,
weight=.95
)



builder.connect(
amount,
operator,
EdgeType.FEATURE,
weight=1
)



builder.connect(
operator,
feature,
EdgeType.FEATURE,
weight=1
)



builder.connect(
feature,
target,
EdgeType.INFERENCE,
weight=.85
)



graph = builder.build()



# extract


extractor = EvidencePathExtractor(
graph
)



paths = extractor.extract_paths(
start=intent.id,
end=target.id
)



# scoring


scorer = EvidenceScorer()


ranker = EvidencePathRanker(
scorer
)



ranked = ranker.rank(
paths
)



selector = TopKSelector(
k=3
)



top_paths = selector.select(
ranked
)



print("\n=== TOP-K EVIDENCE PATHS ===")



for item in top_paths:

    path = item["path"]

    print("\nPATH:")

    print(
        " → ".join(
            n.name
            for n in path.nodes
        )
    )


    print(
        "SCORE:",
        item["score"]
    )