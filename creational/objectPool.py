class ObjectPool:
    def __init__(self, size):
        self._pool = [self._create_object() for _ in range(size)]
        self._used = [False] * size

    def _create_object(self):
        # Create your object here; for example, a simple object like an integer
        return 0

    def acquire(self):
        for i, used in enumerate(self._used):
            if not used:
                self._used[i] = True
                return self._pool[i]
        raise RuntimeError("No objects available in the pool")

    def release(self, obj):
        try:
            index = self._pool.index(obj)
            if self._used[index]:
                self._used[index] = False
        except ValueError:
            pass  
            
if __name__ == "__main__":
    pool = ObjectPool(size=5)
    obj1 = pool.acquire()
    obj2 = pool.acquire()
    print(f"Acquired objects: {obj1}, {obj2}")
    pool.release(obj1)
    pool.release(obj2)
    obj3 = pool.acquire()
    print(f"Acquired object: {obj3}")
    obj4 = pool.acquire()
    obj5 = pool.acquire()
    print(f"Acquired objects: {obj4}, {obj5}")
    pool.release(obj3)
    obj6 = pool.acquire()
    print(f"Acquired object: {obj6}")
