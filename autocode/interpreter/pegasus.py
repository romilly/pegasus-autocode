from collections import defaultdict


class Pegasus():
    def __init__(self, output, program):
        self.output = output
        self.values = defaultdict(int)
        self.program = program
        self.running = False
        self.pc = 0


    def set(self, name, value):
        self.values[name] = value

    def get(self, name):
        return self.values[name]

    def write(self, text):
        self.output.write(text)

    def execute(self):
        next = self.pc
        self.pc += 1
        nextline = self.line(next)
        nextline.evaluate_in(self)

    def line(self, pc):
        return self.program.line(pc)

    def label(self, l):
        return self.program.label(l)

    def run(self):
        self.running = True
        while self.running:
            self.execute()

    def stop(self):
        self.running = False

    def jump_to_label(self, l):
        self.pc = self.label(l)

