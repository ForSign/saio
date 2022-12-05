def dfs(g: list, v: int, used: list, match: list):
    if used[v]:
        return False
    used[v] = True
    for to in g[v]:
        if to == -1:
            continue
        if (match[to] == -1 or dfs(g,match[to], used, match)):
            match[to] = v
            return True 
    return False


def khun(g: list):
    match = [-1 for _ in range(len(g))]
    used  = [False for _ in range(len(g))]
    match = [-1 for _ in range(len(match))]

    for i in range(len(g)):
        used = [False for _ in range(len(used))]
        dfs(g, i, used, match)
    
    res = {}
        
    for i in range(len(g)):
        if match[i] != -1:
            if i < match[i]:
               res[i] = match[i]
            else:
                res[match[i]] = i
                
    return res


if __name__ == "__main__":
    g = [{5}, 
         {5, 6}, 
         {7, 8},
         {6},
         {5, 8},
         {0, 1, 4},
         {1, 3},
         {2},
         {2, 4}]

    print(khun(g))
