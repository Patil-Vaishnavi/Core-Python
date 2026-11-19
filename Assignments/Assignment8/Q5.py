
def check(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return n > 1

def prime(n):
    s = 0
    for i in range(2, n + 1):
        if check(i):
            s += i
    return s

n = 10
print(prime(n))
