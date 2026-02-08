# Hash Table with Chaining

class HashTableChaining:
    def __init__(self, capacity=11):
        self.capacity = max(3, int(capacity))
        self.buckets = [[] for _ in range(self.capacity)]
        self.count = 0

    def _index(self, key):
        return hash(key) % self.capacity

    def load_factor(self):
        return self.count / self.capacity

    def insert(self, key, value):
        i = self._index(key)
        bucket = self.buckets[i]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])
        self.count += 1

    def search(self, key):
        i = self._index(key)
        for k, v in self.buckets[i]:
            if k == key:
                return v
        return None

    def delete(self, key):
        i = self._index(key)
        bucket = self.buckets[i]
        for idx, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(idx)
                self.count -= 1
                return True
        return False

if __name__ == "__main__":
    ht = HashTableChaining()
    ht.insert("a", 1)
    ht.insert("b", 2)
    print("search a:", ht.search("a"))
    print("delete a:", ht.delete("a"))
    print("search a:", ht.search("a"))
