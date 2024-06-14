from heapq import heappush, heappop


print("====================  Min Heap  =======================")


def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


minHeap = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(minHeap)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("====================  Min Heap with tuple =======================")
h = []
heappush(h, (5, 'write code'))
heappush(h, (7, 'release product'))
heappush(h, (1, 'write spec'))
heappush(h, (3, 'create tests'))

print(h)            # [(1, 'write spec'), (3, 'create tests'), (5, 'write code'), (7, 'release product')]
print(heappop(h))   # (1, 'write spec')


print("====================  Max Heap with tuple =======================")
h = []
heappush(h, (-5, 'write code'))
heappush(h, (-7, 'release product'))
heappush(h, (-1, 'write spec'))
heappush(h, (-3, 'create tests'))

print(h)            # [(1, 'write spec'), (3, 'create tests'), (5, 'write code'), (7, 'release product')]
print(heappop(h))   # (1, 'write spec')