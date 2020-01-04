class frac:
	def __init__(self, n=0, d=1):
		self.n=n
		self.d=d

def swap(m, a, b):
    n = []
    size = len(m)
    if a == b:
        return m
    for i in range(size):
        row = []
        tmp = m[i]
        if i == a:
            tmp = m[b]
        if i == b:
            tmp = m[a]
        for j in range(size):
            t = tmp[j]
            if j == a:
                t = tmp[b]
            if j == b:
                t = tmp[a]
            row.append(t)
        n.append(row)
    return n

def stdform(m):
    zero = -1
    if len(m)==1:
        return m
    for i in range(len(m)):
        s = sum([x.n for x in m[i]])
        if s == 0:
            zero = i
        if s!=0 and zero > -1:
            n = swap(m, i, zero)
            return stdform(n)
    return m

def transientstates(m):
    if len(m)==1:
        return 0
    for i in range(len(m)):
        if sum([x.n for x in m[i]]) == 0:
            return i

def rq(m):
    t = transientstates(m)
    s = len(m)
    Q = []
    R = []
    if t==0:
        R.append(m[0])
    for i in range(t):
        Q.append(m[i][:t])
        R.append(m[i][t:s])
    return Q,R

def eye(t):
    I = []
    for i in range(t):
        row = []
        for j in range(t):
            if i==j:
                row.append(frac(1))
            else:
                row.append(frac(0))
        I.append(row)
    return I

def transpose(m):
    t = []
    for i in range(len(m)):
        row = []
        for j in range(len(m)):
            row.append(m[j][i])
        t.append(row)
    return t

def minor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

###
def det(m):
	if len(m)==1:
		return m[0]
	if len(m)==2:
		m1 = frac(m[0][0].n*m[1][1].n, m[0][0].d*m[1][1].d)
		m2 = frac(m[0][1].n*m[1][0].n, m[0][1].d*m[1][0].d)
		x = lcm(m1.d,m2.d)
		return frac((m1.n*x//m1.d) - (m2.n*x//m2.d), x)
	de = frac(0)
	for c in range(len(m)):
		x = det(minor(m,0,c))
		curr = frac(((-1)**c)*m[0][c].n*x.n, m[0][c].d*x.d)
		x = lcm(curr.d, de.d)
		de = frac(curr.n*x//curr.d+de.n*x//de.d,x)
	return de

###
def inverse(m):
    de = det(m)
    s = len(m)
    if s==1:
    	return [frac(m[0].d,m[0].n)]
    if s==2:
        return [[frac(m[1][1].n*de.d, m[1][1].d*de.n), frac(-1*m[0][1].n*de.d,m[0][1].d*de.n)],
                [frac(-1*m[1][0].n*de.d,m[1][0].d*de.n), frac(m[0][0].n*de.d, m[0][0].d*de.n)]]
    cof = []
    for i in range(s):
        row = []
        for j in range(s):
            mi = minor(m,i,j)
            x = det(mi)
            row.append(frac(((-1)**(i+j)) * x.n, x.d))
        cof.append(row)
    cof = transpose(cof)
    for i in range(s):
        for j in range(s):
            cof[i][j] = frac(cof[i][j].n*de.d, cof[i][j].d*de.n)
    return cof

def sub(A, B):
    diff = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            x=lcm(A[i][j].d,B[i][j].d)
            n=A[i][j].n*x//A[i][j].d - B[i][j].n*x//B[i][j].d
            row.append(frac(n,x))
        diff.append(row)
    return diff

def mul(A, B):
    if len(A)==1 and len(B)==1:
        return [frac(A[0].n*B[0].n,A[0].d*B[0].d)]
    m = []
    rows = len(A)
    cols = len(B[0])
    try:
        iters = len(A[0])
    except:
        iters = 1
    for i in range(rows):
        row = []
        for j in range(cols):
            sum = frac(0)
            if iters!=1:
                for k in range(iters):
                    s = frac(A[i][k].n*B[k][j].n, A[i][k].d*B[k][j].d)
                    x = lcm(s.d,sum.d)
                    sum=frac(s.n*x//s.d + sum.n*x//sum.d, x)
            else:
                for k in range(iters):
                    s = frac(A[k].n*B[k][j].n, A[k].d*B[k][j].d)
                    x = lcm(s.d,sum.d)
                    sum=(s.n*x//s.d + sum.n*x//sum.d, x)
            row.append(sum)
        m.append(row)
    return m

def conv(m):
    n = []
    if len(m)==1:
        if m[0]==0:
            return [frac(m[0],1)]
        else:
            return [frac(m[0],m[0])]
    for i in m:
        if sum(i)!=0:
            n.append([frac(x,sum(i)) for x in i])
        else:
            n.append([frac(x,1) for x in i])
    return n

def gcd(a, b):
    while b!=0:
        t = b
        b = a%b
        a = t
    return a

def lcm(a, b):
    return a*b//gcd(a,b)

def findlcm(a):
    if len(a)<2:
        return a
    L = lcm(a[0],a[1])
    for i in range(2,len(a)):
        L = lcm(L, a[i])
    return L

def simplify(x):
	g = gcd(x.n,x.d)
	x = frac(x.n//g, x.d//g)
	return x

def solution(m):
    m = conv(m)
    m = stdform(m)
    t = transientstates(m)
    Q,R = rq(m)
    I = eye(t)
    F = inverse(sub(I,Q))
    if t!=0:
        B = mul(F,R)
    else:
        B = [frac(1)]
    init = []
    init.append(frac(1))
    for i in range(1,t):
        init.append(frac(0))
    ans = mul(init, B)[0]
    if t!=0:
        ans = [frac(x[0],x[1]) for x in ans]
        ans = [simplify(x) for x in ans]
        den = [x.d for x in ans]
        num = [x.n for x in ans]
        L = findlcm(den)
        for i in range(len(num)):
            num[i] *= L//den[i]
        num.append(L)
    else:
        num = [ans.n,ans.d]
    return num
