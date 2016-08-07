import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '../..'))
import unittest
from heap import Heap

class TestHeap(unittest.TestCase):
    def test_insert(self):
        heap = Heap()
        heap.insert(4)
        self.assertEqual(heap.heap, [4])
        heap.insert(3)
        self.assertEqual(heap.heap, [3, 4])
        heap.insert(2)
        self.assertFalse(self.heap_violation(heap.heap))
        heap.insert(1)
        self.assertFalse(self.heap_violation(heap.heap))

    def heap_violation(self, heap):
        for i in range(len(heap)):
            position = i + 1
            key = heap[position - 1]
            parent_position = self.parent_position(position)
            if not parent_position:
                continue
            parent = heap[parent_position - 1]
            if parent > key:
                return True
        return False

    def parent_position(self, position):
        return position / 2

if __name__ == '__main__':
    unittest.main()