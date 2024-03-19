# 재귀함수 => 특정 시점으로 돌아오는게 핵심이다 

# 재귀함수 팁 
# 파라미터 : 바로 작성하지 말고 구조를 먼저 잡는다 

arr= [ i for i in range(1, 4)]
path = [False] * 3
def dfs(level):
    # 기저조건 
    # 이 문제는 3개 뽑을 때 까지 반복한다 
    if level == 3:
        return 
    
    # 다음 재귀 호출을 해야함 
    # 다음에 갈 수 있는 곳은 어디인가 
    
    # 기본코드 
    # path[level] = 1
    # dfs(level + 1)
    
    # path[level] = 2
    # dfs(level+1)
    
    # path[level] = 3
    # dfs(level+1)

    for i in range(len(arr)):
        if arr[i] in path:
            continue
        path[level] = arr [i]
        dfs(level+1)
    