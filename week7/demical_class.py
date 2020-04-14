from decimal import *


class changePrecision:
    def __init__(self, precision):
        if type(precision) is not int:
            raise ValueError('Only int are allowed as precision')
        self.precision = precision

    def __enter__(self):
        getcontext().prec = self.precision
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        getcontext().prec = 28
