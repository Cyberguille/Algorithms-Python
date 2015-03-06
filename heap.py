__author__ = 'ramon'

import heapq

heap = [7, 4, 1, 3, 5, 9]

heapq.heapify(heap)
heapq.heappush(heap, 10)
print(heap)
heapq.heappop(heap)
print(heap)
print(heapq.nsmallest(1, heap))
print(heap)
heapq.heappop(heap)
print(heap)
print(heapq.nlargest(1, heap))
print(heap)