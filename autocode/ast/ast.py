def ioperation(op, left, right):
    return {'+':Plus,'-':Minus,'x':Times,'*':Remainder}[op](left, right)

def operation(op, left, right):
    return {'+':Plus,'-':Minus,'x':Times,'/':Div}[op](left, right)


class Element():
    def __ne__(self, other):
        return not self == other

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__


class Integer(Element):
    def __init__(self, value):
        self.value = int(value)

    def evaluate_in(self, context):
        return self.value

    def __repr__(self):
        return str(self.value)


class Index(Element):
    def __init__(self, name):
        self.name = name

    def evaluate_in(self, context):
        return context.get(self.name)


class IndexAssignment(Element):
    def __init__(self, index, value):
        self.index = index
        self.value = value

    def evaluate_in(self, context):
        context.set(self.index.name, self.value.evaluate_in(context))

class Negated(Element):
    def __init__(self, value):
        self.value = value


class Plus(Element):
   def __init__(self, left, right):
       self.left = left
       self.right = right


class Minus(Element):
   def __init__(self, left, right):
       self.left = left
       self.right = right


class Times(Element):
    def __init__(self, left, right):
       self.left = left
       self.right = right


class Remainder(Element):
    def __init__(self, left, right):
       self.left = left
       self.right = right


class IDiv(Element):
    def __init__(self, left, right):
       self.left = left
       self.right = right

class Div(Element):
    def __init__(self, left, right):
       self.left = left
       self.right = right

class ReadProgramTape(Element):
    pass


class ReadDataTape(Element):
    def __init__(self, qualifier, reader):
        self.qualifier = qualifier
        self.reader = reader


class MultipleIndexAssignment(Element):
    def __init__(self, index, value):
        self.index = index
        self.value = value


class MultipleVariableAssignment(Element):
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value


class MaxInt(Element):
    def evaluate_in(self, context):
        return 8192 # largest index in autocode!


class Variable(Element):
    def __init__(self, id):
        self.id = id

    def evaluate_in(self, context):
        return context.get(self.name_in(context))

    def name_in(self, context):
        return 'v%d' % self.id.evaluate_in(context)

class Print(Element):
    def __init__(self, value, format_spec):
        self.value = value
        self.format_spec = format_spec

    def evaluate_in(self, context):
        val = self.value.evaluate_in(context)
        fmt = self.format_spec.evaluate_in(context)
        context.write(self.format_value(val, fmt))

    def format_value(self, val, fmt):
        return str(val) # TODO: replace with proper formatting


class VariableAssignment(Element):
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value


class Float(Element):
    def __init__(self, float_string):
        self.value = float(float_string)


class Stop(Element):
    pass









