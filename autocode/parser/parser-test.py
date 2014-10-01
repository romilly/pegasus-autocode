import unittest
from autocode.parser import autocode_line


class ParserTest(unittest.TestCase):
    # TODO: TAPEB

    def test_parses_tape_statements(self):
        self.assertTrue(autocode_line.parse('line','TAPE') is not None)
        self.assertTrue(autocode_line.parse('line','n7 = TAPE') is not None)
        self.assertTrue(autocode_line.parse('line','n7 = TAPE n2') is not None)
        self.assertTrue(autocode_line.parse('line','n7 = TAPE *') is not None)
        self.assertTrue(autocode_line.parse('line','v3 = TAPE') is not None)
        self.assertTrue(autocode_line.parse('line','v3 = TAPE n2') is not None)
        self.assertTrue(autocode_line.parse('line','v3 = TAPE *') is not None)

    def test_parses_integer_assignments(self):
        self.assertTrue(autocode_line.parse('line','n1 = 5') is not None)
        self.assertTrue(autocode_line.parse('line','n1 = -5') is not None)
        self.assertTrue(autocode_line.parse('line','n1 = n2') is not None)
        self.assertTrue(autocode_line.parse('line','n1 = n2 + 5') is not None)
        self.assertTrue(autocode_line.parse('line','n1 = n2 - 5') is not None)
        self.assertTrue(autocode_line.parse('line','n1 = n2 x 5') is not None)
        self.assertTrue(autocode_line.parse('line','n1 = n2 * 5') is not None)
        self.assertTrue(autocode_line.parse('line','n1 = n2 + n7') is not None)

    def test_parses_print_statements(self):
        self.assertTrue(autocode_line.parse('line','PRINT v7, 4000') is not None)
        self.assertTrue(autocode_line.parse('line','PRINT n3, 4000') is not None)
        self.assertTrue(autocode_line.parse('line','PRINT v7, n3') is not None)
        self.assertTrue(autocode_line.parse('line','PRINT vn7, 3236') is not None)

    def test_parses_variable_assignments(self):
        self.assertTrue(autocode_line.parse('line','v1 = 5.0') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = -5.0') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = v3') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = v3 + 5') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = v3 x 5') is not None)

    def test_parses_modification(self):
        self.assertTrue(autocode_line.parse('line','vn7 = 323.6') is not None)
        self.assertTrue(autocode_line.parse('line','v(5+n7) = 323.6') is not None)
        self.assertTrue(autocode_line.parse('line','v(5+n7) = v(-7+n5) + v(3+n2)') is not None)
        self.assertTrue(autocode_line.parse('line','vn7 = vn1 + 323.6') is not None)
        self.assertTrue(autocode_line.parse('line','vn7 = vn1 + vn5') is not None)

    def test_parses_functions(self):
        self.assertTrue(autocode_line.parse('line','v1 = MOD 5.0') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = MOD v2') is not None)



    # TODO: Mixed Assignment

    # TODO: Functions

    # TODO: Jump Instructions

    # TODO: STOP instruction


