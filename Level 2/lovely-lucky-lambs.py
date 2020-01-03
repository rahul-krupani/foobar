def solution(total_lambs):
    n1 = FibSum(total_lambs)
    n2 = PowSum(total_lambs)
    return n1-n2

def FibSum(n):
    fib = [1, 1, 0]
    if n < 2:
        return n
    tot = 2
    i = 2
    while tot <= n:
        fib[2] = fib[0] + fib[1]
        tot += fib[2]
        i += 1
        fib[0] = fib[1]
        fib[1] = fib[2]
    i -= 1
    return i

def PowSum(n):
    if n < 2:
        return n
    tot = 1
    i = 1
    while tot <= n:
        i += 1
        tot = 2**i - 1
    i -= 1
    return i

print(solution(143))
