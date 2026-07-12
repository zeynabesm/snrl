class EvidencePathRanker:


    def __init__(self, scorer):

        self.scorer = scorer



    def rank(self, paths):

        ranked = []


        for path in paths:

            score = self.scorer.score(path)


            ranked.append(
                {
                    "path": path,
                    "score": score
                }
            )


        ranked.sort(
            key=lambda x: x["score"],
            reverse=True
        )


        return ranked