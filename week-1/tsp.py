from itertools import permutations

def tsp(G, s) :
    """
    Find out the least distance using Travelling sales person algorithm
    tsp( Graph : 2D List, s : int )

    s is staring node index

    """

    # list of vertices need to traverse
    vertices = list(range(len(G)))

    # except the starting node
    vertices.pop(s)

    # all possible travelling ways
    ways = permutations(vertices)

    # minimum cost
    min_cost = 100000000
    for way in ways:

        # find out the cost on each way

        # intially zero cost
        cost = 0

        # c - current node ==> intially at start
        c = s

        # n - next node in way
        for n in way:
            cost += G[c][n]
            c = n

        # again last node to starting node
        cost += G[c][s]

        # minimizing cost
        if cost < min_cost :
            min_cost = cost

    # return the minimum cost
    return min_cost


if __name__ == "__main__":

    G = [[0, 10, 15, 20],
		[10,  0, 35, 25],
		[15, 35,  0, 30],
		[20, 25, 30, 0]]

    s = 0
    print(tsp(G, s))
