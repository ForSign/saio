g = [[0, 1, 4],
     [1, 3],
     [2],
     [2, 4]]
n = 5
k = 4
mt = []
used = []


def try_kuhn (v):
    if used[v]:
        return False;

    used[v] = True;

    for i in range(g[v].len()):
        to = g[v][i];
        if mt[to] == -1 or try_kuhn (mt[to]):
            mt[to] = v;
            return True;

    return False;


def main():
    mt = [-1] * k;
    for v in range(n):
        used = [False] * n;
        try_kuhn (v);
 
    for i in range(k):
        if mt[i] != -1:
            print (mt[i]+1, "  ", i+1)


if __name__ == "__main__":
    main()