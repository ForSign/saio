import numpy as np
import math
from scipy.optimize import linprog


DEBUF_PRINT = True


def grep_row(c, i, number):
    row = []
    for index, ind in zip(np.zeros(len(c)), range(len(c))):
        if ind == i:
            index = number
        row.append(index)
    return row


def branch_border(c, A, b, bnd):
    x_opt = []
    rec = -np.inf
    stack_ab = list()
    stack_ab.append([A, b])
    while len(stack_ab) > 0:

        next_ilp = stack_ab.pop()
        next_A, next_b = next_ilp[0], next_ilp[1]
        simplex = linprog(c=c, A_ub=next_A, b_ub=next_b, bounds=bnd, method="simplex")
        vector_x = simplex.x

        if DEBUF_PRINT:
            print()
            print('Current Vars \nA: ' + str(next_A) + '\nb: ' + str(next_b))
            print('Vector x: ' + str(vector_x))

        if not simplex.success:
            continue

        float_x, float_indice = None, None

        for xi, x in enumerate(vector_x):
            if x.is_integer():
                continue
            float_x = x
            float_indice = xi

        new_rec = simplex.fun
        
        if DEBUF_PRINT:
            print('Current record: ' + str(new_rec))

        if not float_x:
            if new_rec > rec:
                rec = new_rec
                x_opt = vector_x

        if new_rec <= rec:
            continue

        left_A = next_A.copy()
        left_b = next_b.copy()
        left_A.append(grep_row(c, float_indice, -1))
        left_b.append(math.ceil(float_x))

        right_A = next_A.copy()
        right_b = next_b.copy()
        right_A.append(grep_row(c, float_indice, 1))
        right_b.append(math.floor(float_x))

        stack_ab.append([left_A, left_b])
        stack_ab.append([right_A, right_b])

    return x_opt


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


if __name__ == '__main__':
    DEBUF_PRINT = False
    assert all( branch_border(*test_1) == [3, 2] )
    assert all( branch_border(*test_2) == [4, 3] )
    assert all( branch_border(*test_3) == [5, 2] )
    print("Asserts passed")