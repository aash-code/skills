class TestCase:
    def __init__(self, input, expected):
        self.input = input
        self.expected = expected
        self.actual = None
        
    def set_actual(self, actual):
        self.actual = actual
        
    def status(self):
        if self.actual == self.expected:
            return "PASSED"
        else:
            return "FAILED"    