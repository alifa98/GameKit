
class NegativeNumberException(Exception):

    message = "Numbers should not be negative."

    def __init__(self, message) -> None:
        self.message = message

    def __init__(self) -> None:
        pass
