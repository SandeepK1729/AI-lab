class Graph : 
    def __init__(self, adjacent_nodes, heurlistic_values) : 
        self.adjacent_nodes = adjacent_nodes
        self.H = heurlistic_values
        
    def find_a_star_path(self, start, end) : 
        open_list = [(start : self.H[start])]
        close_list = set() 
        
        while len(open_list) > 0 : 
            c_node, c_cost = open_list.pop(0)
            c_node - self.H[c_node]
            
            for node, cost in self.adjacent_nodes[c_node] : 
                 cost += (c_node - self.H[c_node])
                 open_list.append((node, cost))
                 open_list.sort(key = )
                
