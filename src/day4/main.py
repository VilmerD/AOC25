def readInput(file):
    with open(file) as f:
        X = []
        for row in f:
            x = [0]
            for r in row[:-1]:
                x.append(1 if r == '@' else 0)
            x.append(0)
            X.append(x)
        cols = len(X[0])
        zeros = [0 for i in range(0, cols)]
        X.insert(0, zeros)
        X.append(zeros)
    return X

def print2DArray(X):
    M = len(X)
    for R in X:
        s = ""
        for i in R:
            s = s + str(i)
        print(f"{s}")

def computeNbrs(X):
    M = len(X)
    N = len(X[0])
    
    Y = []
    for r in range(1, M-1):
        y = []
        for c in range(1, N-1):
            nbrs = 0
            for rr in range(-1, 2):
                for cc in range(-1, 2):
                    nbrs += X[r+rr][c+cc]
            nbrs = nbrs - X[r][c]
            y.append(nbrs)
        Y.append(y)
    return Y

def RemoveAccessible(X):
    ## Get sizes
    M = len(X)
    N = len(X[0])
    removed = False

    Y = computeNbrs(X)
    Z = X
    for r in range(1, M - 1):
        for c in range(1, N - 1):
            if (X[r][c] == 1 and Y[r-1][c-1] < 4):
                Z[r][c] = 0
                removed = True
    return Z, removed

def CountX(X):
    ## Get sizes
    M = len(X)
    N = len(X[0])
    cnt = 0

    for r in range(1, M - 1):
        for c in range(1, N - 1):
            if (X[r][c]):
                cnt += 1
    return cnt

def TaskA():
    X = readInput("input.txt")
    Y = computeNbrs(X)

    cnt = 0
    for y, x in zip(Y, X[1:-1]):
        for _y, _x in zip(y, x[1:-1]):
            if (_x == 1 and _y < 4): 
                cnt = cnt + 1

    print(f"Count = {cnt}")

def TaskB():
    X = readInput("input.txt")
    cnt_initial = CountX(X)
    removed = True
    while removed:
        X, removed = RemoveAccessible(X)
    
    cnt_final = CountX(X)
    print(f"Final amount removed: {cnt_initial-cnt_final}")

TaskB()