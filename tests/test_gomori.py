from gomori.gomori import *
import numpy

def test_gomori():
    c = np.array([-21, -11,0])
    A = np.array([[7, 4,1]])
    b = np.array([13])
    bound = [[0, None], [0, None], [0, None]]
    assert numpy.allclose(numpy.array([0, 3]), gomori(c, A, b, bound)[:2])

    c = np.array([-2, -3, 0, 0])
    A = np.array([[1, 4, 1, 0], [2, 3, 0, 1]])
    b = np.array([14, 12])
    bound = [[0, None], [0, None], [0, None], [0, None]]
    assert numpy.allclose(numpy.array([3, 2]), gomori(c, A, b, bound)[:2])
