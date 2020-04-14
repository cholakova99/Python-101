from time import time, sleep
from contextlib import ContextDecorator


class measurePerformance(ContextDecorator):
    def __init__(self):
        self.counter = 0

    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end = time()
        self.total_time = self.end - self.start
        print("Benchmark ended for: ", self.total_time)
        if type(exc_type) is not None:
            return False
        return

    def benchmark(self, message=None, restart=False):
        self.counter += 1
        self.end = time()
        total = self.end - self.start
        if message is None:
            print('Benchmark N', self.counter, ' : ', total)
        else:
            print(message, ":", total)
        self.start = time()
