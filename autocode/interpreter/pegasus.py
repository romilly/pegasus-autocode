from collections import defaultdict


class Pegasus():
    def __init__(self):
        self.values = defaultdict(int)

    def set(self, name, value):
        self.values[name] = value

    def get(self, name):
        return self.values[name]
