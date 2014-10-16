def ioperation(op, left, right):
    return {'+':Plus,'-':Minus,'x':Times,'*':Remainder}[op](left, right)


def operation(op, left, right):
    return {'+':Plus,'-':Minus,'x':Times,'/':Div}[op](left, right)


def comparison(compare, left, right):
    return {'>':GT,'>=':GE,'=*':AE,'/=':NE,'/=*':NAE}[compare](left, right)

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
    def __init__(self, index):
        self.index = int(index)

    def name_for_index_numbered(self, number):
        return "n%d" % number

    def name(self):
        return self.name_for_index_numbered(self.index)

    def number_in(self, context):
         return self.index

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

class Operation(Element):
    def __init__(self, left, right):
       self.left = left
       self.right = right

    def evaluate_in(self, context):
        return self.operation(self.left.evaluate_in(context),self.right.evaluate_in(context))


class Plus(Operation):
    def operation(self,l,r):
        return l + r


class Minus(Operation):
    def operation(self,l,r):
        return l - r


class Times(Operation):
   def operation(self,l,r):
        return l * r


class Remainder(Operation):
    def operation(self,l,r):
        return l % r


class IDiv(Operation):
    def operation(self,l,r):
        return l // r


class Div(Operation):
    def operation(self,l,r):
        return l / r


class ReadProgramTape(Element):
    pass


class ReadDataTape(Element):
    def __init__(self, qualifier, reader):
        self.qualifier = qualifier
        self.reader = reader


class MultipleIndexAssignment(Element):
    def __init__(self, index, source):
        self.index = index
        self.source = source


class MultipleVariableAssignment(Element):
    def __init__(self, variable, source):
        self.variable = variable
        self.source = source


class MaxInt(Element):
    def evaluate_in(self, context):
        return 8192 # largest index in autocode!


class Variable(Element):
    def __init__(self, id):
        self.id = id

    def evaluate_in(self, context):
        return context.get(self.name_in(context))

    def number_in(self, context):
        return self.id.evaluate_in(context)

    def name_for_variable_numbered(self, number):
        return 'v%d' % number

    def name_in(self, context):
        return self.name_for_variable_numbered(self.number_in(context))


class VariableAssignment(Element):
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

    def evaluate_in(self, context):
        context.set(self.variable.name_in(context), self.value.evaluate_in(context))


class Float(Element):
    def __init__(self, float_string):
        self.value = float(float_string)

    def evaluate_in(self, context):
        return self.value


class Stop(Element):
    def evaluate_in(self, context):
        context.stop()


class Jump(Element):
    def __init__(self, target):
        self.target = target

    def evaluate_in(self, context):
        context.jump_to_label(self.target.evaluate_in(context))


class CJump(Element):
    def __init__(self, target, condition):
        self.target = target
        self.condition = condition

    def evaluate_in(self, context):
        if self.condition.evaluate_in(context):
            context.jump_to_label(self.target.evaluate_in(context))


class GT(Operation):
    def operation(self,l,r):
        return l > r


class AE(Operation):
    pass


class GE(Operation):
    def operation(self,l,r):
        return l >= r

class NE(Operation):
    def operation(self,l,r):
        return l != r

class NAE(Operation):
    pass





