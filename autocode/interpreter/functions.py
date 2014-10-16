from math import sin, cos, tan, asin, atan, acos, log, exp
from autocode.interpreter.ast import Element


def fun(function, value):
    fundict = {'MOD':Mod,'INT':Int,'FRAC':Frac,'SQRT':Sqrt,
               'SIN':Sin,'COS':Cos,'TAN':Tan,'CSC':Cosec,'SEC':Sec,'COT':Cot,
               'ARCSIN':Arcsin,'ARCCOS':Arccos,'ARCTAN':Arctan,
               'LOG':Log,'EXP':Exp,'EXPM':Expm}
    return fundict[function](value)


class Function(Element):
    def __init__(self, value):
        self.value = value

    def evaluate_in(self, context):
        self.function(self.value.evaluate_in(context))

class Mod(Function):
    def function(self, x):
        return abs(x)


class Int(Function):
    def function(self, x):
        return int(x)


class Frac(Function):
    def function(self, x):
        return x - int(x)


class Sqrt(Function):
    def function(self, x):
        return x**0.5


class Sin(Function):
    def function(self, x):
        return sin(x)


class Cos(Function):
    def function(self, x):
        return cos(x)

class Tan(Function):
    def function(self, x):
        return tan(x)


class Cosec(Function):
    def function(self, x):
        return 1/cos(x)


class Sec(Function):
    def function(self, x):
        return 1/sin(x)


class Cot(Function):
    def function(self, x):
        return 1/tan(x)

class Arcsin(Function):
    def function(self, x):
        return asin(x)


class Arccos(Function):
   def function(self, x):
        return acos(x)


class Arctan(Function):
    def function(self, x):
        return atan(x)

class Log(Function):
    def function(self, x):
        return log(x)


class Exp(Function):
    def function(self, x):
        return exp(x)


class Expm(Function):
    def function(self, x):
        return exp(-x)











