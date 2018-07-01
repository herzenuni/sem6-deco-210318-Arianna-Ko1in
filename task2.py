import functools

def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            inner.value = func(*args, **kwargs)
            inner.called = True
        return inner.value

    inner.called = False
    return inner


@once
def initialize_settings():
    global called
    called = True
    print("Settings initialized")
    return "value"

called = False
assert initialize_settings()=='value'
assert called

# call one more time to check stored value
called = False
assert initialize_settings()=='value'
assert not called
