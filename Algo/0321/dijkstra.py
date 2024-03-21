import sys
from heapq import heappop, heappush

sys.stdin = open("dijkinput.txt","r")

INF = int(1e9)
V, E = map(int, input().split())

# 인접리스트 
graph = [[] for _ in range(V)]
# 누적 거리를 저장할 변수 
distance = [INF] * V

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])

def dijkstra(start):
    pq = []
    
    heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        # 최단 거리 노드에 대한 정보
        dist, now = heappop(pq)
        
        # now 에서 인접한 다른 노드 확인
        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]
            
            
            # 누적거리 계산 
            new_dist = dist + next_dist
            # 이미 더 짧은 거리로 간 경우 pass
            if new_dist >= distance[next_node]:
                continue
            
            distance[next_node] = new_dist
            heappush(pq, (new_dist, next_node))
dijkstra(0)
print(distance)
