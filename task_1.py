def caching_fibonacci():
    cache = {}
    # function for recursive calculation of Fibonacci numbers
    def fibonacci(n: int):
        # processing logic
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    
    return fibonacci
# assigning a function to a variable
fib = caching_fibonacci()

print(fib(10))
print(fib(15))