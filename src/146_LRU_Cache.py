class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.data = {}
        self.list_node = {}
        self.capacity = capacity

        self.head = Node(-1)
        self.tail = Node(-1)
        self._link_nodes(self.head, self.tail)

    def _link_nodes(self, prev_node, next_node):
        prev_node.next = next_node
        next_node.prev = prev_node

    def _remove(self, key):
        if key not in self.list_node.keys():
            return
        curr_node = self.list_node[key]
        self._link_nodes(curr_node.prev, curr_node.next)
        self.list_node.pop(key)

    def _add(self, key):
        node = Node(key)
        self._link_nodes(node, self.head.next)
        self._link_nodes(self.head, node)
        self.list_node[key] = node

    def _del_last(self):
        last_node = self.tail.prev
        self._link_nodes(last_node.prev, self.tail)
        self.list_node.pop(last_node.key)
        self.data.pop(last_node.key)

    def get(self, key: int) -> int:
        if key in self.data:
            self._remove(key)
            self._add(key)
            return self.data[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.data and len(self.data) == self.capacity:
            self._del_last()
        self._remove(key)
        self._add(key)
        self.data[key] = value


lRUCache = LRUCache(2)
lRUCache.put(1, 1)  # // cache is {1=1}
lRUCache.put(2, 2)  # // cache is {1=1, 2=2}
print(lRUCache.get(1))  # // return 1
lRUCache.put(3, 3)  # // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))  # // returns -1 (not found)
lRUCache.put(4, 4)  # // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))  # // return -1 (not found)
print(lRUCache.get(3))  # // return 3
print(lRUCache.get(4))  # // return 4
