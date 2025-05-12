def check_password(correct_password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            password = input("Enter the password here: ")
            if password != correct_password:
                print("Access denied!")
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator

@check_password('secret_password')
def very_protected_function():
    print("Very sad. There is not secret data")

@check_password('difficult_pass')
def hard_function():
    print("...")

very_protected_function()
hard_function()