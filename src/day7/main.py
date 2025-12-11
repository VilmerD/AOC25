from functools import lru_cache
START = "S"
SPLIT = "^"
BEAM = "|"

def ReadInput(file):
    with open(file) as f:
        lines = []
        for row in f:
            lines.append([c for c in row])
        return lines

def PrintState(X):
    if len(X) < 1:
        print("Array empty")
        return
    L = len(X[0])
    header = "="*L
    print(f"{header}")
    for x in X:
        row = "".join(x)
        print(f"{row[:-1]}")
    print(f"{header}")

def Propagate(X):
    ## Get sizes
    nrows = len(X)
    if nrows < 1:
        print("Array empty")
        return
    ncols = len(X[0])

    ## Initialize values
    splits = 0

    ## Iterate over rows. Skip the last row, do not need to propagate it
    for r in range(0, nrows-1):
        # Iterate over columns
        for c in range(0, ncols):
            chr = X[r][c]
            if chr == START:
                X[r+1][c] = BEAM
            elif chr == BEAM:
                # Check if the next chr is a split, otherwise continue!
                if X[r+1][c] == SPLIT:
                    splits += 1
                    if (c > 0):
                        X[r+1][c-1] = BEAM
                    if (c < ncols-1):
                        X[r+1][c+1] = BEAM
                else:
                    X[r+1][c] = BEAM
    return X, splits
    
def TaskA(file):
    X = ReadInput(file)
    PrintState(X)
    Xnew, splits = Propagate(X)
    PrintState(Xnew)
    print(f"Number of splits : {splits}")


def TaskB(file):
    ## Read input
    X = ReadInput(file)

    ## Get sizes
    nrows = len(X)
    if (nrows < 1):
        return 0
    ncols = len(X[0])

    @lru_cache(maxsize=None)
    def CountNumPaths(r, c):
        ## Update user
        print(f"At [{r}, {c}]")

        # Base case
        if r == nrows - 1:
            return 1
        
        # Otherwise propagate
        if (X[r][c] == SPLIT):
            # Then split and continue counting
            c1 = 0
            c2 = 0
            if (c > 0):
                c1 = CountNumPaths(r, c - 1)
            if (c < ncols - 1):
                c2 = CountNumPaths(r, c + 1)
            return c1 + c2
        else:
            # Else increase row count by one and continue
            return CountNumPaths(r + 1, c)

    ## Initialize values
    paths = 0

    # Find start
    for r in range(0, nrows-1):
        # Iterate over columns
        for c in range(0, ncols):
            chr = X[r][c]
            if chr == START:
                paths = CountNumPaths(r+1, c)
    
    print(f"Found {paths} paths")

TaskB("input.txt")
