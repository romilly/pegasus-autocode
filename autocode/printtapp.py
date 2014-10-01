# coding: utf8
__author__ = 'romilly'


class Translator():
    def __init__(self):
        self.letters = True

    def from_tape(self, ch):
        val = ord(ch)
        if val == 0:
            self.letters = False
            return ''
        if val == 27:
            self.letters = True
            return ''
        if self.letters:
            return '|ABCDEFGHIJKLMNOPQRSTUVWXYZ .?£@'[val]
        return '|12*4()78#=-v\n ,0>g3^56/x9+ .n\r%'[val]

with open("plan/resources/pegem/PROGRAMS/E.TAP",'rb') as tap:
    translator = Translator()
    while(True):
        line = tap.readline()
        if not line:
            break
        print [translator.from_tape(ch) for ch in line]