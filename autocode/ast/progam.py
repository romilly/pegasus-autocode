class Program():
    def __init__(self, *lines):
        self.lines = lines
        self.labels = {0:0}
        for (number, line) in enumerate(lines):
            if line.label is not None:
                self.labels[line.label] = number

    def line(self, pc):
        return self.lines[pc]

    def label(self, number):
        return self.labels[number]
    

class Line():
    def __init__(self, statement, label=None, flag=None):
        self.statement = statement
        self.label= label
        self.flag = flag

    def evaluate_in(self, context):
        self.statement.evaluate_in(context)

