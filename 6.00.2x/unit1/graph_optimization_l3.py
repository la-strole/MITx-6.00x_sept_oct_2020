# edges = [(1, 2), (1, 2), (1, 4), (2, 4), (2, 3), (2, 3), (3, 4)]
# edges = [(1,2), (1,4), (2,4), (2,3), (3,4)]
edges = [(1, 2), (1, 2), (1, 4), (2, 4), (2, 3), (3, 4)]
current_node = 1
n = [current_node]
count = [1]


def rec_graph(edges, current_node):
    """"
    my code for Kenigsberg bridges problem
    """
    # 1 base cases
    way_list = [item for item in edges if current_node in item]

    if len(edges) == 0:
        print(f'answer - YES, path={n}')
        return True
    elif len(way_list) == 0:
        print(f'{count[0]}. no way from here, path={n}')
        count[0] += 1
        n.pop()
        return False  # no way from current node
    else:
        # 2 find all possible paths from start node
        way_no_duplicate = set(way_list)
        node_return = []
        for way in way_no_duplicate:
            new_edge = edges.copy()
            new_edge.remove(way)
            if way[0] == current_node:
                new_node = way[1]
            else:
                new_node = way[0]
            n.append(new_node)
            node_return.append(rec_graph(new_edge, new_node))
    answer = False
    for item in node_return:
        answer = answer or item
    if not answer:
        n.pop()
    return answer


print(rec_graph(edges, current_node))


class Node:
    def __init__(self, name):
        self.name = str(name)

    def get_node_name(self):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Node({self.get_node_name()})'


class Edge:
    def __init__(self, src, dest):
        assert isinstance(src, Node)
        assert isinstance(dest, Node)
        self.src = src
        self.dest = dest

    def get_edge(self):
        return f'{self.src.get_node_name}->{self.dest.get_node_name()}'

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def __str__(self):
        return f'{self.src.get_node_name}->{self.dest.get_node_name()}'


class Digraph:
    def __init__(self):
        self.graph = {}  # keys - nodes, values - list of edges

    def add_node(self, node):
        assert isinstance(node, Node)
        assert node not in self.graph.keys(), 'node is already in graph'
        self.graph[node] = []

    def add_edge(self, edge):
        assert isinstance(edge, Edge)
        try:
            self.graph[edge.get_src()].append(edge)
        except KeyError:
            self.graph[edge.get_src()] = [edge]

    def children_of(self, node):
        assert isinstance(node, Node)
        try:
            children = []
            for edges in self.graph[node]:
                children.append(edges.get_dest())
            return children
        except KeyError:
            print('no such node in graph')

    def __str__(self):
        for key in self.graph.keys():
            print(f'{key.get_node_name()}->{[x.get_dest().get_node_name() for x in self.graph[key]]}')
        return ''


class Graph(Digraph):

    def add_edge(self, edge):
        assert isinstance(edge, Edge)
        try:
            self.graph[edge.get_src()].append(edge)
        except KeyError:
            self.graph[edge.get_src()] = [edge]
        tmp_src = edge.get_dest()
        tmp_dest = edge.get_src()
        try:
            self.graph[tmp_src].append(Edge(tmp_src, tmp_dest))
        except KeyError:
            self.graph[tmp_src] = [Edge(tmp_src, tmp_dest)]


g = Graph()
nodes = [Node(str(x)) for x in range(1, 5)]
for item in nodes:
    g.add_node(item)

edges = [Edge(nodes[0], nodes[1]),
         Edge(nodes[0], nodes[1]),
         Edge(nodes[1], nodes[2]),
         Edge(nodes[1], nodes[2]),
         Edge(nodes[0], nodes[3]),
         Edge(nodes[2], nodes[3]),
         Edge(nodes[3], nodes[1])]

for edge in edges:
    g.add_edge(edge)

print(g)



def DFS(graph: Graph, start: Node, end: Node, path: list, shortest):

    path = path + [start]  # not path.append() - path = path + [list] - new id
    #print(path)
    if start == end:
        return path
    for node in graph.children_of(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest)
                if newPath != None:
                    shortest = newPath
    return shortest


def shortest_path(graph, start, end):
    return DFS(graph, start, end, [], None)


print(shortest_path(g, nodes[0], nodes[3]))

# path остается и в конце он не меняется, те даже когда есть пути в end - все равно не работет