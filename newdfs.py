from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        print(self.graph)

    def edge(self, a, b):
        self.graph[a].append(b)
        

    def dfs(self, b, flags):
        flags = []
        flags[b] = True
        print(flags)

        print(b, end = ' ')

        for i in self.graph[b]:
            if flags[i] == False:
                self.dfs(i, flags)

    def d(self, b):

        flags = [False] * (len(self.graph))
        
        self.dfs(b, flags)

gr = Graph()
print(gr)
gr.edge(1, 2)
gr.edge(1, 3)
gr.edge(2, 4)
gr.edge(2, 3)
gr.edge(3, 4)


gr.d(1)