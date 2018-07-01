import functools

def store(func):
    def decorator(*args, **kwargs):
        if 'source' in kwargs.keys():
            return func
        print("Call from decorator")
        return func(*args, **kwargs)

    return decorator

@store
def inner():
    print("Inner function")
    return True

# call via decorator
assert inner.__name__ == 'decorator'
assert inner()

# extract undecorated function
undecorated = inner(source=True)
assert undecorated.__name__=='inner'

# check for function type
assert(callable(undecorated))
# call undecorated function
assert undecorated()
