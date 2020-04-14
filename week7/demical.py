from decimal import *
from contextlib import contextmanager


@contextmanager
def change_precision(x):
    try:
        getcontext().prec = x
        yield
    except Exception as error:
        raise error
    finally:
        getcontext().prec = 28
