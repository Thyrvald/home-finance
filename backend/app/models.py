

def log(function):
    def wrapper(*args, **kwargs):
        print(f"Executed: {function.__name__} with arugments args = {args}, kwargs = {kwargs}")
        return function(*args, **kwargs)
    return wrapper

@log
def app(foo):
    for i in foo:
        print(i)

def cache(function):
    saved_results = {}
    def wrapper(n):
        if n in saved_results:
            print(f"Cache hit: {n}")
            return saved_results[n]
        result = function(n)
        saved_results[n] = result
        return result
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


