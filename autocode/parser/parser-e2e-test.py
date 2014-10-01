import unittest
from autocode.parser.parser import parse_string


class E2EParserTest(unittest.TestCase):
    def test_recognises_variable_assigment(self):
        code = """
T
D
n1 = n23
1) PRINT n1, 2013
n1 = 5
^0"""
        parse_string(code)


