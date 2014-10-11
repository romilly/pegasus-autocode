from collections import defaultdict


class Pegasus():
    def __init__(self, output):
        self.output = output
        self.values = defaultdict(int)

    def set(self, name, value):
        self.values[name] = value

    def get(self, name):
        return self.values[name]

    def write(self, text):
        self.output.write(text)
