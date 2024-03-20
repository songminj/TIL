# 1~5 번까지의 노드가 존재

# 1. make set
def make_set(n):
    return [i for i in range(n)]

parents = make_set(7)
print(parents)
# 2. find set : 대표자를 찾아보자 
# 부모 노드를 보고 부모 노드도 연결이 되어 있다면 다시 반복
# 언제까지? 자기 자신이 대표인 데이터를 찾을 때 까지  
def find_set(x):
    # 자기 자신이 대표일 때 끝낸다
    if parents[x] == x:
        return x
    return find_set(parents[x])

# 3. union
def union(x, y):
    x = find_set(x)
    y = find_set(y)
    
    # 이미 같은 집합에 속해있다면 continue
    if x == y:
        return
    
    # 다음 집합이라면 합친다
    # 예 ) 더 작은 루트노드에 합쳐라 
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

union(1, 3)
union(2, 3)
union(5, 6)




