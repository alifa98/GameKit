class NegativeNumberException(Exception):
    """Exception raised for negative numbers.
    """

    def __init__(self, message, value):
        self.message = message if message else "Negative numbers are not allowed."
        self.value = value
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} -> {self.value}"
