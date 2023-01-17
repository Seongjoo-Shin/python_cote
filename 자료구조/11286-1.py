# heap

import heapq as hq
import sys

input = sys.stdin.readline # 빠른 입출력 sys.stdin.readline()
pq = [] # 우선순위 큐
for _ in range(int(input())):
  #x = int(input()) # 파이썬은 느린 언어라서 기본 input함수 사용시 시간 초과가 날수 있음
  x = int(input())
  if x:
    hq.heappush(pq, (abs(x), x))
  else:
    print(hq.heappop(pq)[1] if pq else 0)