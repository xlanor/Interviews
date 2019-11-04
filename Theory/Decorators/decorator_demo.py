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

# With syntactic sugar
random_fn(True)
random_fn(False)

def random_fn_2(arg1):
    print("Inner function ran")
    if arg1:
        raise Exception
    print("No exception :)")

# Now, rewrite it without syntactic sugar.
print("==================")
catch_all(random_fn_2)(True)
catch_all(random_fn_2)(False)

# I kind of blew this - I panicked too much during the interview.