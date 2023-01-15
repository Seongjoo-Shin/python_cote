# heap

import heapq as hq
import sys

input = sys.stdin.readline
min_heap = [] # 양수
max_heap = [] # 음수
for _ in range(int(input())):
  x = int(input())
  if x:
    if x > 0:
      hq.heappush(min_heap, x)
    else:
      hq.heappush(max_heap, -x) # 최대힙의 역할을 하고자할 때 -를 붙혀서 넣어줌
  else:
    if min_heap:
      if max_heap:
        if min_heap[0] < abs(-max_heap[0]):
          print(hq.heappop(min_heap))
        else:
          print(-hq.heappop(max_heap))
      else:
        print(hq.heappop(min_heap))
    else:
      if max_heap:
        print(-hq.heappop(max_heap))
      else:
        print(0)