from contextlib import contextmanager


class silenceException:
    def __init__(self, exc_type, message=None):
        self.exc_type = exc_type
        self.message = message

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        same_type = self.exc_type == exc_type
        correct_mes = self.message is None or self.message == str(exc_traceback)
        return same_type and correct_mes


@contextmanager
def silence_exception(exc_type, message=None):
    try:
        yield
    except exc_type as error:
        if message is not None and str(error) != message:
            raise error
