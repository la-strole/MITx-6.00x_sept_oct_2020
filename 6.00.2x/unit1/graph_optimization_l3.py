# edges = [(1, 2), (1, 2), (1, 4), (2, 4), (2, 3), (2, 3), (3, 4)]
#edges = [(1,2), (1,4), (2,4), (2,3), (3,4)]
edges = [(1, 2), (1, 2), (1, 4), (2, 4), (2, 3), (3, 4)]
current_node = 1
n = [current_node]
count = [1]
def rec_graph(edges, current_node):
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
