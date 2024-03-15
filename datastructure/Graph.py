

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, e, v):
        if e not in self.graph:
            self.graph[e] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[e].append(v)
        self.graph[v].append(e)

    def display_graph(self):
        for k, v in self.graph.items():
            print(k, v)

graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1,3)
graph.display_graph()



class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def display(self):
        for row in self.graph:
            print(row)

# Example usage:
num_vertices = 4
my_graph = Graph(num_vertices)
my_graph.add_edge(0, 1)
my_graph.add_edge(0, 2)
my_graph.add_edge(1, 2)
my_graph.add_edge(2, 3)

my_graph.display()


