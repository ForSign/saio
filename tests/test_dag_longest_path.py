from dag_longest_path.dag_longest_path import *


def test_dag_longest_path():
    graph = {
            1: [[2, 6],
                [2, 1]],
            2: [[3],
                [2]],
            3: [[5, 4],
                [1, 8]],
            4: [[],
                []],
            5: [[4],
                [1]],
            6: [[2, 3, 5],
                [4, 5, 1]]
        }
    s = 1
    t = 4

    assert max_way(graph, s, t) == (15, [1, 6, 2, 3, 4])

    graph = {
        1: [[2, 3],
            [5, 3]],
        2: [[3, 4],
            [2, 6]],
        3: [[4, 5, 6],
            [7, 4, 2]],
        4: [[5, 6],
            [-1, 1]],
        5: [[6],
            [-2]],
        6: [[],
            []]
    }
    s = 1
    t = 6

    assert max_way(graph, s, t) == (15, [1, 2, 3, 4, 6])
