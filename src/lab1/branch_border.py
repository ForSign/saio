import numpy as np
import math
from scipy.optimize import linprog


def grep_row(c, ind, number):
    """ Creates canonical boundary row """
    row = []
    for ix, i in zip(np.zeros(len(c)), range(len(c))):
        if i == ind:
            ix = number
        row.append(ix)
    return row


def branch_border(c, A, b, bnd):
    x = []
    r = -np.inf
    stack = list()
    stack.append([A, b])
    while len(stack) > 0:

        nextAb = stack.pop()
        A, b = nextAb[0], nextAb[1]
        res = linprog(c=c, A_ub=A, b_ub=b, bounds=bnd, method="simplex")
        v_x = res.x

        if not res.success:
            continue

        fx, fi = None, None

        for xi, xv in enumerate(v_x):
            if xv.is_integer():
                continue
            fx = xv
            fi = xi

        new_r = res.fun

        if not fx:
            if new_r > r:
                r = new_r
                x = v_x

        if new_r <= r:
            continue

        lA = A.copy()
        lb = b.copy()
        lA.append(grep_row(c, fi, -1))
        lb.append(math.ceil(fx))

        rA = A.copy()
        rb = b.copy()
        rA.append(grep_row(c, fi, 1))
        rb.append(math.floor(fx))

        stack.append([lA, lb])
        stack.append([rA, rb])

    return x


if __name__ == '__main__':
    print(branch_border(*(
        # c
        [-1, -1],
        # A
        [[5, 9],
         [9, 5]],
        # b
        [63, 63],
        # bnd
        [(1, 6),
         (1, 6)])))
