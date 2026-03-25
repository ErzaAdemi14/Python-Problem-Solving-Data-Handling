def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Function name: {func.__name__}")
        print(f"Input: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Output: {result}")
        return result
    return wrapper


@log_function
def add(a, b):
    return a + b


add(3, 5)