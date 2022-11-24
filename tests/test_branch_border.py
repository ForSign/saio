from lab1.branch_border import *


def test_branch_border():
    test_1 = (
        # c
        [-1, -1],
        # A
        [[2, 11],
         [1, 1],
         [4, -5]],
        # b
        [38, 7, 5],
        # bnd
        [(0, np.inf),
         (0, np.inf)])

    test_2 = (
        # c
        [-7, -9],
        # A
        [[-1, 3],
         [7, 1]],
        # b
        [6, 35],
        # bnd
        [(0, np.inf),
         (0, np.inf)])

    test_3 = (
        # c
        [-2, -3],
        # A
        [[3, 4],
         [2, 5]],
        # b
        [24, 22],
        # bnd
        [(0, np.inf),
         (0, np.inf)])

    test_4 = (
        # c
        [-1, -1],
        # A
        [[5, 9],
         [9, 5]],
        # b
        [63, 63],
        # bnd
        [(1, 6),
         (1, 6)])

    assert all( branch_border(*test_1) == [3, 2] )
    assert all( branch_border(*test_2) == [4, 3] )
    assert all( branch_border(*test_3) == [5, 2] )
    assert all( branch_border(*test_4) == [4, 4] )
