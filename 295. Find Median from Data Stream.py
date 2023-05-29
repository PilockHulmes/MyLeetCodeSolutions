import heapq

class MedianFinder:

    def __init__(self):
        self.left = [] # max heap
        self.right = [] # min heap


    def addNum(self, num: int) -> None:
        # all operations in self.left will provide negative value since we want self.left to be a max heap
        heapq.heappush(self.left, - num)
        heapq.heappush(self.right, - heapq.heappop(self.left))
        if len(self.right) > len(self.left) + 1:
            value = heapq.heappop(self.right)
            heapq.heappush(self.left, -value)

    def findMedian(self) -> float:
        if len(self.right) > len(self.left):
            return self.right[0]
        return ((-self.left[0]) + self.right[0]) / 2

obj = MedianFinder()
obj.addNum(1)
print(obj.left, obj.right)
obj.addNum(2)
# print(obj.findMedian())
print(obj.left, obj.right)
obj.addNum(3)
# print(obj.findMedian())
print(obj.left, obj.right)
# print()