import unittest
from listavg import ListAverage

class TestListAverage(unittest.TestCase):
    def test(self):
        lavg = ListAverage([1, 2, 3])
        assert lavg.compute_avg() == 2.0

    # add more unit tests below
    def test_faster(self):
        lavg = ListAverage([2,4,6])
        self.assertTrue(lavg.compute_avg_faster(), 4.0)

    def test_faster_with_add(self):
        lavg = ListAverage([2,4,6])
        lavg.add(8)
        self.assertTrue(lavg.compute_avg_faster(), 5.0)
