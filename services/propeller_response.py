from core.exception.exceptions import WrongInputException


class PropellerStatObject:
    def __init__(self, res):
        for num in res:
            if num not in ["result", "meta"]:
                raise WrongInputException("WRONG INPUT")
        self.result = res['result']
        self.meta = res['meta']

    def __str__(self):
        return '{} - {}'.format(self.result, self.meta)

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        if self.result == other.result and self.meta == other.meta:
            return True
        return False
