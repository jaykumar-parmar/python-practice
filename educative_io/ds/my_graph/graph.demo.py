from my_graph import MyGraph

graph = MyGraph()
graph.addVertex('Anna')
graph.addVertex('Bob')
graph.addVertex('Frank')
graph.addVertex('Jane')

graph.addEdges('Anna', ['Bob', 'Frank'])
graph.addEdges('Bob', ['Anna', 'Frank'])
graph.addEdges('Frank', ['Anna', 'Bob', 'Jane'])
graph.addEdges('Jane', ['Frank'])

graph.dfs()