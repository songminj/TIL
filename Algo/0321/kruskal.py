# kruskal
# 전체 그래프를 보고, 가중치가 가장 작은 간선부터 뽑기. 

import sys
sys.stdin = open("input.txt","r")

def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    
    if x == y:
        return
    if x < y :
        parents[y] = x
    else:
        parents[x] = y
    

V, E = map(int, input().split())
edges = []
for _ in range(E):
    s,e, w = map(int, input().split())
    edges.append([s, e, w])
edges.sort(key=lambda x: x[2]) 

# 대표자 배열
parents = [ i for i in range(V) ]

# Mst 완성은 

sum_weight = 0
cnt = 0 
# 간선을 모두 확인한다
for s, e, w in edges:
    # 사이클이 발생하면 pass
    if find_set(s) == find_set(e):
        print(s, e, w, ' / 사이클발생 탈락!')
        continue
    
    cnt += 1
    # 사이클이 없으면 통과 
    union(s, e)
    sum_weight += w
    if cnt == V -1 :
        break
    
print(f'최소 비용 = {sum_weight}')
