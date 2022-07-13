import time


def timeit(func):
    def timed(*args, **kwargs):
        print("Function [start]:", func.__name__)
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        print("Function [end]:", func.__name__, "(", round((te - ts) * 1000, 1), "ms)")
        print()
        return result

    return timed
