class TopKSelector:



    def __init__(self, k=3):

        self.k = k



    def select(self, ranked_paths):

        return ranked_paths[:self.k]