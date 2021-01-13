# 크루스칼 알고리즘 코드 작성
# 제일먼저 그래프 구기


graphs = {
    'vertices': ['A','B','C','D','E','F','G'],
    'edges' : [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}


parent = dict()
rank = dict() # height 표현하기위해! 이게 필요함 크루스칼 알고리즘에선


def find(node):
    # path compression 기법 필요
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2 # 하지만 이경우에는 root 1, 2 둘다 랭크 길이가 같은경우도 있기때문에, 만약 같을경우에는 ..
        if rank[root1] == rank[root2]:
            rank[root2] += 1 # 루트노드의 랭크에 1을 추가해줘서 랭크 길이를 더 높여주면 된다.






def make_set(node):
    parent[node] = node # 부모노드는 자기위에 노드가 없으니까, 자기 자신을 가리키게 하기
    rank[node] = 0


def kruskal(graph):
    answer = []

    for node in graph['vertices']:
        make_set(node)

    edges = graphs['edges']
    edges.sort()

    # 간선연결! 사이클이 없는 간선들만 answer 에 추가해주기 !
    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u): # 루트노드 같지 않으면, 사이클이 없는거고 그럴때 union 으로 트리 두개 합치
            union(node_v, node_u)
            answer.append(edge)

    return answer


print(kruskal(graphs))