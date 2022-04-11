import unittest


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    size = 16

    def __init__(self):
        self.store = [None] * self.size

    def get(self, key):
        index = hash(key) & 15
        if self.store[index] is None:
            return None
        n = self.store[index]
        while True:
            if n.key == key:
                return n.value
            else:
                if n.next:
                    n = n.next
                else:
                    return None

    def set(self, key, value):
        nd = Node(key, value)
        index = hash(key) & 15
        n = self.store[index]
        if n is None:
            self.store[index] = nd
        else:
            if n.key == key:
                n.value = value
            else:
                while n.next:
                    if n.key == key:
                        n.value = value
                        return
                    else:
                        n = n.next
                n.next = nd
    def delete(self, index):
        if index is not None:
            del self.store[index]

class Threemap:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def set(self, value):
        if self.value is None:
            self.value = value
        else:
            if value < self.value:
                if self.left is None:
                    self.left = Threemap(value)
                else:
                    self.left.set(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Threemap(value)
                else:
                    self.right.set(value)

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.value)
        if self.right:
            self.right.printTree()




class MapTestMixin:

    hm = HashMap()
    hm.set("8", "8")
    hm.set("9", "9")
    hm.set("10", "10")
    hm.set("11", "11")
    print(hm.get("8"))
    print(hm.get("9"))
    print(hm.get("10"))
    print(hm.get("11"))

    map_cls = None

    def setUp(self) -> None:
        self.hash_map = self.map_cls()

    def test_simple(self):
        tree = Threemap(5)
        tree.set(8)
        tree.set(7)
        tree.set(2)
        tree.set(4)
        tree.set(3)
        tree.set(1)
        tree.set(9)
        tree.printTree()

    def test_raise_key_error(self):
        with self.assertRaises(KeyError):
            i = self.hash_map[1]



class HashMapTest(MapTestMixin, unittest.TestCase):
  map_cls = dict


class TreeMapTest(MapTestMixin, unittest.TestCase):
  map_cls = dict


unittest.main(argv=[''], verbosity=2, exit=False)
