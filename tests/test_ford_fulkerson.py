from ford_fulkerson.ford_fulkerson import *

def test_ford_fulkerson():
    matrix = [[0, 7, 4, 0, 0, 0],
              [0, 0, 4, 0, 2, 0],
              [0, 0, 0, 8, 4, 0],
              [0, 0, 0, 0, 4, 5],
              [0, 0, 0, 0, 0, 12],
              [0, 0, 0, 0, 0, 0]]
    start = 0
    end = 5

    assert method_ford_fulkerson(start, end, len(matrix), matrix)[0] == 10

    matrix = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

    start = 0
    end = 5

    assert method_ford_fulkerson(start, end, len(matrix), matrix)[0] == 23