import unittest


class HashMap:
    def __init__(self):
        self.size = 16
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size
    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        print('_______________________________тест_______________________________')
        for item in self.map:
            if item is not None:
                print(str(item))
class MapTestMixin:
    h = HashMap()
    h.add('Дима', '7 991 558-39-59')
    h.add('Илья', '7 991 252-64-41')
    h.add('Никита', '7 991 558-38-79')
    h.add('Саня', '7 985 265-21-59')
    h.add('Гоша', '7 985 084-73-51')
    h.add('Равиль', '7 991 620-21-28')
    h.add('Раиль', '7 991 620-22-70')
    h.add('Слава', '7 991 181-01-54')
    h.print()
    h.delete('Слава')
    h.print()
    print('Гоша: ' + h.get('Гоша'))

class HashMapTest(MapTestMixin, unittest.TestCase):
  map_cls = dict

unittest.main(argv=[''], verbosity=2, exit=False)