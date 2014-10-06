def operation(op, left, right):
    return {'+':Plus,'-':Minus,'x':Times,'*':Mod}[op](left, right)


class Element():
    def __ne__(self, other):
        return not self == other

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__


class Modifier(Element):
    def __init__(self, integer, index):
        self.integer = integer
        self.index = index


class Integer(Element):
    def __init__(self, value):
        self.value = int(value)

    def evaluate_in(self, context):
        return self.value

    def __repr__(self):
        return str(self.value)


class Index(Element):
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)


class IndexAssignment(Element):
    def __init__(self, index, value):
        self.index = index
        self.value = value

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

class Mod(Element):
    def __init__(self, left, right):
       self.left = left
       self.right = right


