from igeg.edge import EdgeType



class EvidenceScorer:


    def __init__(
        self,
        alpha=0.30,
        beta=0.25,
        gamma=0.25,
        delta=0.20,
        lambda_complexity=0.05
    ):

        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.delta = delta
        self.lambda_complexity = lambda_complexity



    def semantic_score(
        self,
        path
    ):

        scores=[]


        for edge in path.edges:

            if edge.edge_type == EdgeType.SEMANTIC:

                scores.append(
                    edge.weight
                )


        return self._average(scores)



    def relational_score(
        self,
        path
    ):

        scores=[]


        for edge in path.edges:


            if edge.edge_type in [
                EdgeType.RELATIONAL,
                EdgeType.MAPPING
            ]:

                scores.append(
                    edge.weight
                )


        return self._average(scores)



    def feature_score(
        self,
        path
    ):

        scores=[]


        for edge in path.edges:


            if edge.edge_type == EdgeType.FEATURE:

                scores.append(
                    edge.weight
                )


        return self._average(scores)



    def inference_score(
        self,
        path
    ):

        scores=[]


        for edge in path.edges:


            if edge.edge_type == EdgeType.INFERENCE:

                scores.append(
                    edge.weight
                )


        return self._average(scores)



    def complexity_penalty(
        self,
        path
    ):

        length=len(
            path.edges
        )


        return min(
            length * 0.01,
            0.1
        )



    def score(
        self,
        path
    ):


        semantic = self.semantic_score(path)

        relational = self.relational_score(path)

        feature = self.feature_score(path)

        inference = self.inference_score(path)


        penalty = self.complexity_penalty(
            path
        )


        final_score = (

            self.alpha * semantic

            +

            self.beta * relational

            +

            self.gamma * feature

            +

            self.delta * inference

            -

            self.lambda_complexity * penalty

        )


        final_score = round(
            final_score,
            3
        )


        path.set_score(
            final_score
        )


        return final_score



    def breakdown(
        self,
        path
    ):


        return {

            "semantic_alignment":
                self.semantic_score(path),


            "schema_validity":
                self.relational_score(path),


            "feature_quality":
                self.feature_score(path),


            "inference_strength":
                self.inference_score(path),


            "complexity_penalty":
                self.complexity_penalty(path),


            "final_score":
                path.score

        }



    def _average(
        self,
        values
    ):

        if not values:

            return 0


        return round(
            sum(values)/len(values),
            3
        )