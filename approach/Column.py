from approach.config.imports import *


from approach.Textual import Textual
from approach.Numerical import Numerical

class Column(object):

    def __init__(self, name, values):
        self.name   = name
        self.values = values
        self.type   = self.getType()

    def getType(self):
        numerical = 0
        textual   = 0
        total     = 0

        for val in self.values:
            if not self.isNan(val):
                if self.isNumber(val):
                    numerical = numerical + 1
                else:
                    textual = textual + 1
                total = total + 1

        if textual == 0 and numerical == total:
            return "numerical"
        elif numerical == 0 and textual == total:
            return "textual"
        else:
            return "mixed"

    def isNumber(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def isNan(self, value):
        try:
            value = float(value)
            math.isnan(value)
            return True
        except ValueError:
            return False
