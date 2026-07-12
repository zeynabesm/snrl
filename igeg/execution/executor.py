import pandas as pd



class DatasetExecutor:


    def __init__(self, database):

        self.database = database



    def run(self, sql):


        columns, rows = (

            self.database.execute(sql)

        )


        dataframe = pd.DataFrame(

            rows,

            columns=columns

        )


        return dataframe



    def split_target(
        self,
        dataframe,
        target
    ):


        X = dataframe.drop(
            columns=[target]
        )


        y = dataframe[target]


        return X, y