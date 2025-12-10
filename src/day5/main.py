def getNumber(string, i0):
    j = i0
    while (j < len(string) and string[j].isdigit()):
        j = j + 1
    return j

def getRange(row):
    i = 0
    # Get number 
    j = getNumber(row, i)
    x0 = int(row[i:j])      

    # Skip dash
    i = j + 1           

    # Get next number
    j = getNumber(row, i)
    xe = int(row[i:j])          
    return (x0, xe)

def readIds():
    ids = []
    with open("ids.txt") as f:
        for row in f:
            ids.append(int(row))   
    return ids

def readRanges():
    ranges = []
    with open("ranges.txt") as f:
        for row in f:
            ranges.append(getRange(row))
    return ranges
     
def countFresh():
    ranges = readRanges()
    ids = readIds()
    cnt = 0
    for num in ids:
        for ra in ranges:
            if num in range(ra[0], ra[1]):
                cnt += 1
                break
    print(f"Count of all fresh in list = {cnt}")

"""
    Takes rangesA and removes rangesB
"""
def BooleanSum(rangesA, rangeB):
    found = False
    rangesOut = []
    for rangeA in rangesA:
        if (rangeB[1] < rangeA[0] - 1 or rangeA[1] < rangeB[0] - 1):
            # A             |-----|
            # B |-----| 
            #
            # or 
            #
            # A |-----|
            # B             |-----| 
            rangesOut.append(rangeA)
        else:
            # A |-----|
            # B    |-----| 
            newMin = min(rangeA[0], rangeB[0])
            newMax = max(rangeA[1], rangeB[1])
            rangesOut.append((newMin, newMax))
            found = True
    if not found:
        rangesOut.append(rangeB)
    return rangesOut

def updateRanges():
    ## Get ranges
    ranges = readRanges()
    ranges = sorted(ranges, key=lambda range: range[0])

    ## Get boolean sum of all ranges
    ranges_sum = [ranges[0]]
    for ra in ranges:
        ranges_sum = BooleanSum(ranges_sum, ra)

    ## Get sum
    for ra in ranges_sum:
        print(f"{ra[0]}-{ra[1]}")

    ## Count size of all ranges
    cnt = 0
    for ra in ranges_sum:
        cnt += ra[1] - ra[0] + 1
    print(f"Count of all fresh = {cnt}")

countFresh()
updateRanges()