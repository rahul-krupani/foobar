def conv(dim, coord, box):
    mirror_rotation=[2*coord, 2*(dim-coord)]
    if(box<0):
        for i in range(box, 0):
            coord-=mirror_rotation[(i+1)%2]
    else:
        for i in range(box, 0, -1):
            coord+=mirror_rotation[i%2]
    return coord 
        

def dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

def gcd(a, b):
    if a==0:
        return 1
    while b!=0:
        tmp = b
        b = a%b
        a = tmp
    return a

def vec(coord):
    h = gcd(abs(coord[0]),abs(coord[1]))
    return [coord[0]//h, coord[1]//h]

def mirrordim(dims, pos, boxx, boxy):
    x = conv(dims[0], pos[0], boxx)
    y = conv(dims[1], pos[1], boxy)
    return [x, y]

def solution(dimensions, your_position, guard_position, distance):
    maxx = (distance//dimensions[0])+1
    maxy = (distance//dimensions[1])+1
    vectors = dict()
    for i in range(-maxx, maxx+1):
        for j in range(-maxy, maxy+1):
            loc = mirrordim(dimensions, guard_position, i, j)
            d = dist(your_position, loc)
            v = (your_position[0]-loc[0],your_position[1]-loc[1])
            loc = vec(v)
            if not tuple(loc) in vectors and d<=distance:
                vectors[tuple(loc)] = d
            elif tuple(loc) in vectors and d<=distance: 
                if d<vectors[tuple(loc)]:
                    vectors[tuple(loc)] = d
    
    for i in range(-maxx, maxx+1):
        for j in range(-maxy, maxy+1):
            loc = mirrordim(dimensions, your_position, i, j)
            d = dist(your_position, loc)
            v = (your_position[0]-loc[0],your_position[1]-loc[1])
            loc = vec(v)
            if tuple(loc) in vectors:
                if d<=vectors[tuple(loc)]:
                    vectors.pop(tuple(loc))
    return len(vectors)

print(solution([3,2], [1,1], [2,1], 4))
