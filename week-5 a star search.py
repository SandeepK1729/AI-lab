class Graph:
    """Class to find less cost path using A* star Informed Search algorithm"""

    def __init__(self, adjancency_matrix, H):
        self.H = H
        self.adjancency_matrix = adjancency_matrix

    def find_a_star_path(self, start, end):
        open_list = [(start, self.H[start], start)]

        while len(open_list) > 0:

            current_node, current_cost, current_path = open_list.pop(0)

            if current_node == end:
                return (current_cost - self.H[end], current_path)

            for node, cost in self.adjancency_matrix[current_node]:

                cost += (current_cost - self.H[current_node]) + self.H[node]
                open_list.append((node, cost, f"{current_path} -> {node}"))

            open_list.sort(key=lambda x: x[1])

        return "No path exist"


if __name__ == "__main__":
    H = {'A': 1, 'B': 1, 'C': 1, 'D': 1}
    A = {
        'A': [('B', 1), ('C', 3), ('D', 7)],
        'B': [('D', 5)],
        'C': [('D', 12)]
    }

    graph = Graph(A, H)
    cost, path = graph.find_a_star_path('A', 'D')
    print(f"cost : {cost}")
    print(f"path : {path}")
