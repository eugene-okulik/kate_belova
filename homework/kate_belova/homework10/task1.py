def finish_me(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('finished')
        return result

    return wrapper


@finish_me
def hello_world():
    print('Hello, World!')


hello_world()
