
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)


def fib2(n):
    result = [-1 for i in range(n+1)]
    def items(n):
        if n==1 or n==2:
            return 1
        if result[n] > 0:
            return result[n]
        result[n] = items(n-1) + items(n-2)
        return result[n]
    return items(n)

import time
start = time.time()
print(fib(40))
mid = time.time()
print(fib2(40))
end = time.time()
print(mid-start, end-mid)