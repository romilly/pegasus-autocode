__author__ = 'romilly'


class SimpleIndex():
    def __init__(self, name):
        self.number = int(name[1:])

    def __repr__(self):
        return 'n%d' % self.number

class Label():
    def __init__(self, label):
        self.number = int(label[:-1])

class Integer():
    def __init__(self, value):
        self.value = value

    def evaluate_in(self, context):
        return self.value

    def __repr__(self):
        return str(self.value)


class Program():
    def __init__(self):
        self.directives = []
        self.statements = []
        self.labels = {0: 0}

    def append_directive(self, directive):
        self.directives.append(directive)

    def append(self, statement):
        self.statements.append(statement)

    def append_labelled(self, label, statement):
        self.labels[label] = len(self.statements)
        self.statements.append(statement)


class Assignment():
    def __init__(self, target, value):
        self.target = target
        self.value = value

    def __repr__(self):
        return '= '.join([repr(self.target), repr(self.value)])

