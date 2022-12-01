import numpy as np
from scipy.optimize import linprog
from math import trunc, ceil


def get_f(a):
  return 1 - (ceil(a) - a)


def gomori(c, A, b, bound):
    while True:

        res = linprog( c, A, b, bounds = bound, method = 'simplex')

        x = res.x
        Jb = []
        for i in range(len(x)):
            if x[i] != 0:
              Jb.append(i + 1)

        while len(Jb) < len(A):
            for i in range(len(A[0])):
                if i + 1 not in Jb:
                    Jb.append(i + 1)
                    break

        k = None
        flag = 0
        for i in range(len(x)):
            if abs(round(x[i]) - x[i]) > 10 ** -6:
                k = i
                flag = 1
                break

        if flag == 0:
            return x

        ab = np.array([np.copy(A[:,i-1]) for i in Jb]).transpose()
        ab_inv = np.linalg.inv(ab)

        l = [0 for i in range(len(Jb))]
        l[k] = 1
        y = np.dot(l, ab_inv)
        small_a = []

        for i in range(len(A[0])):
            small_a.append(np.dot(y, A[:,i]))

        small_b = np.dot(y, b)
        Jnb = [i for i in range(1, len(c) + 1) if i not in Jb]
        new_a = [0 for _ in range(len(A[0]))]

        for i in range(len(Jnb)):
            new_a[Jnb[i] - 1] = -get_f(small_a[Jnb[i] - 1])
        new_a += [1]
        arr = A.tolist()

        for i in arr:
            i += [0]

        arr.append(new_a)
        A = np.array(arr)
        arr = c.tolist()
        arr += [0]

        c = np.array(arr)
        arr = b.tolist()
        arr += [-get_f(small_b)]
        b = np.array(arr)

        bound.append([0, None])


if __name__ == '__main__':
    c = np.array([-21, -11,0])
    A = np.array([[7, 4,1]])
    b = np.array([13])
    bound = [[0, None], [0, None], [0, None]]

    # c = np.array([-2, -3, 0, 0])
    # A = np.array([[1, 4, 1, 0], [2, 3, 0, 1]])
    # b = np.array([14, 12])
    # bound = [[0, None], [0, None], [0, None], [0, None]]

    print(gomori(c, A, b, bound))