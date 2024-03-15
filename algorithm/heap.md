## 힙구조

힙은 특정한 규칙을 가지는 트리로, 최댓값과 최솟값을 찾는 연산을 빠르게 하기 위해 고안된 완전이진트리를 기본으로 한다. 

힙 property : A가 B의 부모노드이면 A의 키값과 B의 키값 사이에는 대소 관계가 성립한다

최소 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 작은 힙
최대 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 큰 힙


`import heapq`를 사용하여 문제를 해결한다. 최소힙을 기준으로 한다. 

```buildoutcfg
heapq.heappush(heap, item) : item을 heap에 추가
heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨. 
heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )

```

```buildoutcfg
# BOJ 1927. 최소 힙

import sys
import heapq
# n : 연산의 개수
n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num:
        heapq.heappush(heap, num)
    else:
        if heap:
            min_value = heapq.heappop(heap)
            print(min_value)
        else:
            print(0)
```

만약 최대 힙을 구하고 싶다면 y = -x의 형태로 정렬을 시켜준다. 
힙에 원소를 추가할 때 (-item, item)을 해주면 구현을 해줄 때 최대 힙 구현에 활용된다. 