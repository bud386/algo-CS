import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    
# print(graph)
q = deque()
cnt_node = []
visited = [0] * (N+1)

for leaf_node in range(1, len(graph)):
    # 리프 노드 탐색해서 q에 넣고 bfs
    if graph[leaf_node] == []:
        q.append(leaf_node)
        cnt = 0
        visited[leaf_node] = 1

        while q:
            now = q.pop()
            # 부모 노드 탐색해서 q에 넣어줌
            for p_node in range(1, len(graph)):
                if now in graph[p_node] and visited[p_node] == 0:
                    visited[p_node] = 1
                    q.append(p_node)
                    cnt += 1
        cnt_node.append([cnt, leaf_node])
# print(visited)
# 리프 노드가 있어서 cnt_node에 추가되어 있다면
ans = []
if cnt_node:
    max_cnt = max(cnt_node)[0]
    if visited.count(0) - 1 >= max_cnt:
        for i in range(1, len(visited)):
            if visited[i] == 0:
                ans.append(i)

    for i in cnt_node:
        if i[0] == max_cnt:
            ans.append(i[1])
else:
    for i in range(1,N+1):
        print

        
print(*sorted(ans))
