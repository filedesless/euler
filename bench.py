from timeit import timeit


def bench(f, n, *kwargs):
    """Simple benchmark for a given function

    Args:
        f: the function to run
        n: number of times to run
        kwargs: arguments for f
    """
    t = timeit(lambda: f(*kwargs), number=n)
    print(f"{f.__name__}{kwargs} = {f(*kwargs)} ran {n} times in {t}s")
