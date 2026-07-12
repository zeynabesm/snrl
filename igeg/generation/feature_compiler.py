class FeatureExpressionCompiler:


    def compile(self, feature):


        # اگر expression قبلا ساخته شده باشد
        if "expression" in feature:


            return {

                "expression":
                    feature["expression"],


                "name":
                    feature["name"]

            }



        # حالت خام FeaturePlan

        source = feature["source"]

        operator = feature["operator"]


        return {

            "expression":
                f"{operator}({source})",


            "name":
                feature["name"]

        }