from autocode.ast.ast import Element


def fun(function, value):
    fundict = {'MOD':Mod,'INT':Int,'FRAC':Frac,'SQRT':Sqrt,
               'SIN':Sin,'COS':Cos,'TAN':Tan,'CSC':Cosec,'SEC':Sec,'COT':Cot,
               'ARCSIN':Arcsin,'ARCCOS':Arccos,'ARCTAN':Arctan,
               'LOG':Log,'EXP':Exp,'EXPM':Expm}
    return fundict[function](value)


class Mod(Element):
    def __init__(self, value):
        self.value = value


class Int(Element):
    def __init__(self, value):
        self.value = value


class Frac(Element):
    def __init__(self, value):
        self.value = value


class Sqrt(Element):
    def __init__(self, value):
        self.value = value


class Sin(Element):
    def __init__(self, value):
        self.value = value


class Cos(Element):
    def __init__(self, value):
        self.value = value

class Tan(Element):
    def __init__(self, value):
        self.value = value


class Cosec(Element):
    def __init__(self, value):
        self.value = value


class Sec(Element):
    def __init__(self, value):
        self.value = value


class Cot(Element):
    def __init__(self, value):
        self.value = value


class Arcsin(Element):
    def __init__(self, value):
        self.value = value


class Arccos(Element):
    def __init__(self, value):
        self.value = value


class Arctan(Element):
    def __init__(self, value):
        self.value = value


class Log(Element):
    def __init__(self, value):
        self.value = value


class Exp(Element):
    def __init__(self, value):
        self.value = value


class Expm(Element):
    def __init__(self, value):
        self.value = value











