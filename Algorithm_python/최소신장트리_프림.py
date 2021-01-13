import heapq
import collections


edges = [
    (7, 'A', 'B'),
    (5, 'A', 'D'),
    (8, 'B', 'C'),
    (9, 'B', 'D'),
    (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'),
    (6, 'D', 'F'),
    (8, 'E', 'F'),
    (9, 'E', 'G'),
    (11, 'F', 'G')
]


def prim(start_node, edges):
    answer = []
    adj_edges = collections.defaultdict(list)

    for weight, n1, n2 in edges:
        adj_edges[n1].append((weight, n1, n2))
        adj_edges[n2].append((weight, n2, n1))

    connected_nodes = set(start_node)

    candidate_edge_list = adj_edges[start_node]
    heapq.heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heapq.heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            answer.append((weight, n1, n2))

            for edge in adj_edges[n2]:
                heapq.heappush(candidate_edge_list, edge)

    return answer






print(prim('A', edges))