from test_full_igeg import graph
from igeg.path.extractor import EvidencePathExtractor
from igeg.path.evidence import EvidencePath
from igeg.path.scorer import EvidenceScorer



intent = None
target = None



for node in graph.nodes.values():

    if node.node_type.value == "intent":

        intent = node


    if node.node_type.value == "target":

        target = node



extractor = EvidencePathExtractor(
    graph
)



paths = extractor.find_paths(
    intent.id,
    target.id
)



print("\n=== FOUND PATHS ===")



for p in paths:


    nodes = [
        graph.nodes[i]
        for i in p
    ]


    print(
        " -> ".join(
            n.name
            for n in nodes
        )
    )
