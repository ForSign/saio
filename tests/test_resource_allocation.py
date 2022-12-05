from resource_allocation.resource_allocation import *


def test_resource_allocation():
    c = 5
    n = 3

    g = [[1, 2, 3, 4, 5],
         [0, 1, 2, 4, 7],
         [2, 2, 3, 3, 5]]

    assert resource_allocation(g, c, n) == [3, 0, 1]