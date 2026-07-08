from collections import deque


class EvidencePathExtractor:

    def __init__(self, graph):
        self.graph = graph


    def find_path(self, start_node, end_node):
        """
        Find all possible paths using BFS
        """

        queue = deque()

        queue.append(
            [
                {
                    "node": start_node
                }
            ]
        )

        visited = set()


        while queue:

            path = queue.popleft()

            current = path[-1]["node"]


            if current.id == end_node.id:
                return self._format_path(path)


            if current.id in visited:
                continue

            visited.add(current.id)


            for edge in self.graph.get_outgoing_edges(current.id):

                next_node = self.graph.get_node(edge.target)


                new_path = path + [
                    {
                        "edge": edge,
                        "node": next_node
                    }
                ]


                queue.append(new_path)


        return None



    def _format_path(self, path):

        result = []

        for item in path:

            if "node" in item:

                node = item["node"]

                result.append(
                    {
                        "node_name": node.name,
                        "node_type": node.node_type.value
                    }
                )


            if "edge" in item:

                edge = item["edge"]

                result.append(
                    {
                        "edge_type": edge.edge_type.value,
                        "weight": edge.weight,
                        "metadata": edge.metadata
                    }
                )


        return result



    def print_path(self, path):

        print("\n=== Evidence Path ===\n")


        for item in path:


            if "node_name" in item:

                print(
                    f"{item['node_type']} : {item['node_name']}"
                )


            else:

                print(
                    f"   --[{item['edge_type']}] "
                    f"(weight={item['weight']})-->"
                )