arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10]


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, child):
        if not self.left:
            self.left = child
            return
        if not self.right:
            self.right = child
            return
        return
    
    def inorder(self):
        if self != None:
            # 왼쪽이 있으면 계속 탐색
            if self.left:
                self.left.inorder()
                
            print(self.value, end = ' ')
            if self.right:
                self.right.inorder()
                

nodes = [ TreeNode(i) for i in range(0, 14)]

for i in range(0, len(arr), 2):
    parent_node = arr[i]
    child_node = arr[i+1]
    nodes[parent_node].insert(nodes[child_node])
    
# nodes[1].inorder()








# 코테에서는 간단하게
nodes = [[] for _ in range(14)]
for i in range(0, len(arr), 2):
    parent_node = arr[i]
    child_node = arr[i+1]
    nodes[parent_node].append(child_node)


# 자식이 없다는 걸 표시하기 위해 None

for li in nodes:
    for _ in range(len(li), 2):
        li.append(None)


# 중위순회 구현

def inorder(nodeNum):
    # 갈 수 없다면 리턴해라
    if nodeNum == None:
        return
    inorder(nodes[nodeNum][0])
    print(nodeNum, end = ' ')
    inorder(nodes[nodeNum][1])
    
inorder(1)