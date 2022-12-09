from resource_allocation.resource_allocation import *


def test_resource_allocation():
    c = 5
    n = 3

    y = [0, 1, 2, 3, 4, 5]
    g = [[0, 1, 2, 3, 4, 5],
         [0, 0, 1, 2, 4, 7],
         [0, 2, 2, 3, 3, 5]]

    assert resource_allocation(y, g, n, c) == [0, 5, 0]

    c = 4
    assert resource_allocation(y, g, n, c) == [1, 0 ,3]