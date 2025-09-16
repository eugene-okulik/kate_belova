# Easier
def repeat_me(func):
    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)
        for _ in range(count):
            func(*args, **kwargs)

    return wrapper


@repeat_me
def greet_person(name):
    print(f'Hello {name}!')


greet_person(name='Eugene', count=2)


# Harder
def repeat_me(count=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat_me(count=3)
def greet_world(text):
    print(text)


greet_world(text='Hello World!')
