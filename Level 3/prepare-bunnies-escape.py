class Queue:
    def __init__(self):
        self.items = []
    def empty(self):
        return self.items==[]
    def put(self, item):
        self.items.insert(0, item)
    def get(self):
        return self.items.pop()
class coord:
    def __init__(self, x=0, y=0, dist=0):
        self.x = x
        self.y = y
        self.dist = dist

def bfs(map, source):
    n = len(map)
    m = len(map[0])
    q = Queue()
    q.put(source)
    distances = dict()
    distances[(source.x,source.y)] = 1
    while not q.empty():
        curr = q.get()
        
        if curr.x-1 >= 0 and map[curr.x-1][curr.y]!=1 and not (curr.x-1,curr.y) in distances:
            q.put(coord(curr.x-1,curr.y,curr.dist+1))
            distances[(curr.x-1,curr.y)] = curr.dist+1
        
        if curr.x+1 < n and map[curr.x+1][curr.y]!=1 and not (curr.x+1,curr.y) in distances:
            q.put(coord(curr.x+1,curr.y, curr.dist+1))
            distances[(curr.x+1,curr.y)] = curr.dist+1
        
        if curr.y-1 >= 0 and map[curr.x][curr.y-1]!=1 and not (curr.x,curr.y-1) in distances:
            q.put(coord(curr.x,curr.y-1, curr.dist+1))
            distances[(curr.x,curr.y-1)] = curr.dist+1
        
        if curr.y+1 < m and map[curr.x][curr.y+1]!=1 and not (curr.x,curr.y+1) in distances:
            q.put(coord(curr.x,curr.y+1, curr.dist+1))
            distances[(curr.x,curr.y+1)] = curr.dist+1

    return distances

def removewall(map, wall, startdist, enddist):
    moves = []
    n = len(map)
    m = len(map[0])

    if wall.x-1 >= 0 and map[wall.x-1][wall.y] != 1:
        moves.append((wall.x-1, wall.y))
    if wall.x+1 < n and map[wall.x+1][wall.y] != 1:
        moves.append((wall.x+1, wall.y))
    if wall.y-1 >= 0 and map[wall.x][wall.y-1] != 1:
        moves.append((wall.x, wall.y-1))
    if wall.y+1 < m and map[wall.x][wall.y+1] != 1:
        moves.append((wall.x, wall.y+1))
    best = 2**32-1
    
    for start in moves:
        for end in moves:
            if start == end:
                continue
            else:
                if start in startdist and end in enddist:
                    best = min(startdist[start]+enddist[end]+1,best)
    return best

def solution(map):
    n = len(map)
    m = len(map[0])
    source = coord(0,0,1)
    destination = coord(n-1, m-1,1)
    optimal = n + m - 1
    startdist = bfs(map, source)
    if (destination.x,destination.y) in startdist:
        best = startdist[(destination.x,destination.y)]
    else:
        best = 2**32-1
    if best == optimal:
        return best
    enddist = bfs(map, destination)
    for i in range(n):
        for j in range(m):
            if map[i][j]==1:
                possible = removewall(map, coord(i,j), startdist, enddist)
                best = min(possible, best)
    return best
                

print(solution([ [0, 0, 0, 0],
      [1, 1, 1, 0],
      [1, 0, 1, 0],
      [1, 1, 1, 0],
      [1, 0, 0, 0],
      [1, 0, 1, 1],
      [1, 0, 0, 0] ]))
