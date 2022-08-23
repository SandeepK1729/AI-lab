class A_star:
    """Class to find less cost path using A* star Informed Search algorithm"""

    def __init__(self, adjancency_matrix, H):
        self.H = H
        self.adjancency_matrix = adjancency_matrix

    def find_a_star(self, start, end):
        open_list = [(start, self.H[start])]

        while len(open_list) > 0:

            print(open_list)
            current_node, current_cost = open_list.pop(0)

            if current_node == end:
                return (current_cost - self.H[end])

            for node, cost in self.adjancency_matrix[c_node]:

                cost += (current_cost - self.H[current_node]) + self.H[node]
                open_list.append((node, cost))

            open_list.sort()

        return "No path exist"


if __name__ == "__main__":
    H = {'A': 1, 'B': 1, 'C': 1, 'D': 1}
    A = {
        'A': [('B', 1), ('C', 3), ('D', 7)],
        'B': [('D', 5)],
        'C': [('D', 12)]
    }
	
    a = A_star(A, H)
    print(a.find_a_star('A', 'C'))
