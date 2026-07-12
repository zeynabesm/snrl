class AliasManager:


    def __init__(self):

        self.aliases = {}



    def get_alias(self, table):

        if table not in self.aliases:

            prefix = table[0].lower()

            count = len(self.aliases)

            self.aliases[table] = (
                prefix + str(count)
            )


        return self.aliases[table]