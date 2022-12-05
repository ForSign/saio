from khun.khun import *


def test_khun():
    g = [{5}, 
         {5, 6}, 
         {7, 8},
         {6},
         {5, 8},
         {0, 1, 4},
         {1, 3},
         {2},
         {2, 4}]

    assert khun(g) == {0: 5, 1: 6, 2: 7, 4: 8}