# 간단하게 말하자면 리스트 내에서 가장 작은 값이 맨처음에 위치시키는 내장 모듈
import heapq

heap = []
heapq.heappush(heap, 50)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
heapq.heappush(heap, 2)
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)

print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))