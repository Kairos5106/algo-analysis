# dictionary containing each node in the pyramids' chambers and references to their adjacent nodes
graph = {
    1: [2, 6],
    2: [1, 3],
    3: [2, 8],
    4: [5],
    5: [4, 10],
    6: [1, 11],
    7: [8, 12],
    8: [3, 7, 9, 13],
    9: [8, 10],
    10: [5, 9, 15],
    11: [6, 12],
    12: [7, 11, 17],
    13: [8, 18],
    14: [19],
    15: [10, 20],
    16: [17, 21],
    17: [12, 16, 22],
    18: [13, 23],
    19: [14, 20],
    20: [15, 19],
    21: [16],
    22: [17],
    23: [18, 24],
    24: [23, 25],
    25: [24]
}

# code for depth-first search
def dfs(graph, node):
    visited = set()
    stack = []

    visited.add(node)
    stack.append(node) 

    while stack:
        target = stack.pop()
        print(target, end = ' ')

        for vertex in reversed(graph[target]):
            if vertex not in visited:
                visited.add(vertex)
                stack.append(vertex)

# code for breadth-first search
def bfs(graph, node):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        target = queue.pop(0)
        print(target, end = ' ')

        for adjecent_node in graph[target]:
            if adjecent_node not in visited:
                visited.append(adjecent_node)
                queue.append(adjecent_node)

def main():
    bfs(graph, 1)

main()