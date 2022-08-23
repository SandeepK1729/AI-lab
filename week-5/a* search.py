class A_star : 
  def __init__(self, a, H) : 
    self.H = H 
    self.a = a 
    
  def find_a_star(self, start, end) :
    open_list = [(start, self.H[start])]
    
    while len(open_list) > 0 : 
      print ( open_list )
      c_node, c_cost = open_list.pop(0) 
      if c_node == end : 
        return (c_cost - self.H[end])
      for node, cost in self.a[c_node] : 
        cost += c_cost - self.H[c_node] + self.H[node]
        open_list.append((node, cost))
      open_list.sort() 

if __name__ == "__main__" : 
  H = { 'A' : 1, 'B' : 1,'C' : 1,'D' : 1 }
  A= {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
  }
  a = A_star(A, H)
  print(a.find_a_star('A', 'C'))
