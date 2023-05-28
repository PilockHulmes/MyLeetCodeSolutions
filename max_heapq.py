import heapq

class MaxHeapq:
    
    def __init__(self):
        self.heap = []
    
    def push(self, elem):
        elem = - elem
        heapq.heappush(self.heap, elem)
    
    def pop(self):
        elem = heapq.heappop(self.heap)
        return - elem
    
    def pushpop(self, elem):
        elem = - elem
        result = heapq.heappushpop(self.heap, elem)
        return - result
    
    def replace(self, elem):
        elem = - elem
        result = heapq.heapreplace(self.heap, elem)
        return - result

max_heap = MaxHeapq()

max_heap.push(1)
max_heap.push(2)
max_heap.push(3)
max_heap.push(4)
print(max_heap.pop())
print(max_heap.pop())
print(max_heap.pop())
print(max_heap.pop())