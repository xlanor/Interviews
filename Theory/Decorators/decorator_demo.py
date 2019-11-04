# A generic catchall decorator
def catch_all(func):
    def wrapper(arg1):
        try:
            print(f"Received {arg1}")
            func(arg1)
        except Exception as e:
            print("Caught Exception")
    return wrapper

@catch_all
def random_fn(arg1):
    print("Inner function ran")
    if arg1:
        raise Exception
    print("No exception :)")

random_fn(True)
random_fn(False)