"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start = 0):
        "intialize a starting point"
    self.start = self.next = start

    def __repr__ (self):
        """show representation """"

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """returns the next number in sequential order"""
        self.next += 1
        return self.next

    def reset(self):
        self.next = self.start




