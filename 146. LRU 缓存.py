

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity


    def get(self, key: int) -> int:
        value = self.cache.get(key, -1)
        if value != -1:
            value = self.cache.pop(key)
            self.cache[key] = value
        return value


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                leastRecentKey = list(self.cache.keys())[0]
                self.cache.pop(leastRecentKey)
            self.cache[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
c = LRUCache(2)
c.put(1, 1)
c.put(2, 2)