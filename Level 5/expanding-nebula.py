transforms = {
    ((0, 0), (0, 0)): 0,
    ((0, 0), (0, 1)): 1,
    ((0, 0), (1, 0)): 1,
    ((0, 0), (1, 1)): 0,
    ((0, 1), (0, 0)): 1,
    ((0, 1), (0, 1)): 0,
    ((0, 1), (1, 0)): 0,
    ((0, 1), (1, 1)): 0,
    ((1, 0), (0, 0)): 1,
    ((1, 0), (0, 1)): 0,
    ((1, 0), (1, 0)): 0,
    ((1, 0), (1, 1)): 0,
    ((1, 1), (0, 0)): 0,
    ((1, 1), (0, 1)): 0,
    ((1, 1), (1, 0)): 0,
    ((1, 1), (1, 1)): 0
}

def columnsolution(col):
    global transforms
    c = [(0, 0), (0, 1), (1, 0), (1, 1)]
    predecessors = []
    #iteritems for python 2.7
    for k,v in transforms.items():
        if col[0] == v:
            predecessors.append(k)
    for i in range(1, len(col)):
        nextpred = []
        for prev in predecessors:
            for x in c:
                if transforms[(prev[i], x)] == col[i]:
                    t = list(prev)
                    t.append(x)
                    nextpred.append(t)
        predecessors = tuple(nextpred)
    predecessors = tuple([tuple(zip(*x)) for x in predecessors])
    nums = []
    for row in predecessors:
        a = sum([1<<i if c==1 else 0 for i,c in enumerate(row[0])])
        b = sum([1<<i if c==1 else 0 for i,c in enumerate(row[1])])
        nums.append((a,b))
    return nums

def solution(g):
    g = list(zip(*g))
    nums = columnsolution(g[0])
    rightmost = {}
    for i in nums:
        if i[1] in rightmost:
            rightmost[i[1]] += 1
        else:
            rightmost[i[1]] = 1
    for i in range(1, len(g)):
        nums = columnsolution(g[i])
        temp = {}
        for i in nums:
            if i[0] in rightmost:
                if i[1] in temp:
                    temp[i[1]] += rightmost[i[0]]
                else:
                    temp[i[1]] = rightmost[i[0]]
        rightmost = temp
    return sum(rightmost.values())

print(solution([[True, False, True], [False, True, False], [True, False, True]]))
