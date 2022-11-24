def fib(n, memo={}):

    if n <= 2:
        return 1

    memo[n] = fib(n-1, memo) + fib(n-2, memo)

    return memo[n]


print(fib(6))