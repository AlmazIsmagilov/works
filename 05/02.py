def check_password(func):
    def wrapper(*args, **kwargs):
        password = input("Enter password: ")
        if password != "secret":
            print("Access denied.")
            return None
        return func(*args, **kwargs)
    return wrapper

@check_password
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

