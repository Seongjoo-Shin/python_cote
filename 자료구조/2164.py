# Queue
from collections import deque

N = int(input())
dq = deque(range(1, N + 1)) # 1, 2, 3, ..., N

while len(dq) > 1:
  dq.popleft()
  dq.append(dq.popleft())
  if len(dq) == 1:
    break

print(dq.popleft())

