import unittest
from autocode.parser import autocode_line

class ParserTest(unittest.TestCase):

    def test_parses_tape_statements(self):
        self.assertTrue(autocode_line.parse('line','TAPE') is not None)
        self.assertTrue(autocode_line.parse('line','n7 = TAPE') is not None)
        self.assertTrue(autocode_line.parse('line','n7 = TAPE n2') is not None)
        self.assertTrue(autocode_line.parse('line','n7 = TAPE *') is not None)
        self.assertTrue(autocode_line.parse('line','v3 = TAPE') is not None)
        self.assertTrue(autocode_line.parse('line','v3 = TAPE n2') is not None)
        self.assertTrue(autocode_line.parse('line','v3 = TAPE *') is not None)
        self.assertTrue(autocode_line.parse('line','n7 = TAPEB') is not None)

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
        self.assertTrue(autocode_line.parse('line','v1 = 5') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = v3') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = v3 + 5') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = v3 + 5') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = v3 x 5.0') is not None)

    def test_parses_mixed_assignments(self):
        self.assertTrue(autocode_line.parse('line','n1 = v2') is not None)
        self.assertTrue(autocode_line.parse('line','n1 = -v2') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = n2') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = n2/n3') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = 2/n3') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = 2/3') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = n2/3') is not None)


    def test_parses_modification(self):
        self.assertTrue(autocode_line.parse('line','vn7 = 323.6') is not None)
        self.assertTrue(autocode_line.parse('line','v(5+n7) = 323.6') is not None)
        self.assertTrue(autocode_line.parse('line','v(5+n7) = v(-7+n5) + v(3+n2)') is not None)
        self.assertTrue(autocode_line.parse('line','vn7 = vn1 + 323.6') is not None)
        self.assertTrue(autocode_line.parse('line','vn7 = vn1 + vn5') is not None)

    def test_parses_functions(self):
        self.assertTrue(autocode_line.parse('line','v1 = MOD v2') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = -MOD v2') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = INT 5.6') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = INT v2') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = -INT v2') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = FRAC v2') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = SQRT v2') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = SIN v2') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = COS v2') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = TAN v2') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = CSC v2') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = SEC v2') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = COT v2') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = ARCSIN v2') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = ARCCOS v2') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = ARCTAN v2') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = LOG v2') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = EXP v2') is not None)
        self.assertTrue(autocode_line.parse('line','v1 = EXPM v2') is not None)
        self.assertTrue(autocode_line.parse('line','n1 = MOD n2') is not None)
        self.assertTrue(autocode_line.parse('line','n1 = -MOD n2') is not None)

    def test_parses_stop(self):
        self.assertTrue(autocode_line.parse('line','STOP') is not None)

   # using ^ instead of ->

    def test_parses_jump_instructions(self):
        self.assertTrue(autocode_line.parse('line','^0') is not None)
        self.assertTrue(autocode_line.parse('line','^n1') is not None)
        self.assertTrue(autocode_line.parse('line','^0, v2 > v3') is not None)
        self.assertTrue(autocode_line.parse('line','^0, v2 > 3.0') is not None)
        self.assertTrue(autocode_line.parse('line','^0, -v2 > 3.0') is not None)
        self.assertTrue(autocode_line.parse('line','^0, v2 > -3.0') is not None)
        self.assertTrue(autocode_line.parse('line','^0, n2 > -3') is not None)
        self.assertTrue(autocode_line.parse('line','^0, n2 = -3') is not None)
        self.assertTrue(autocode_line.parse('line','^0, n2 = -3') is not None)
        self.assertTrue(autocode_line.parse('line','^0, n2 = -3') is not None)
        self.assertTrue(autocode_line.parse('line','^0, n2 = -3') is not None)
        self.assertTrue(autocode_line.parse('line','^0, v1 =* v3') is not None)
        self.assertTrue(autocode_line.parse('line','^(-4 +n8), v1 =* v3') is not None)

    def test_processes_print_prefixes(self):
        self.assertTrue(autocode_line.parse('line','XP n1 = MOD n2') is not None)
        self.assertTrue(autocode_line.parse('line','X n1 = MOD n2') is not None)
        self.assertTrue(autocode_line.parse('line','SP n1 = MOD n2') is not None)
        self.assertTrue(autocode_line.parse('line','S n1 = MOD n2') is not None)

    def test_parses_bracketed_interludes(self):
        self.assertTrue(autocode_line.parse('line','(^0)') is not None)
        self.assertTrue(autocode_line.parse('line','^0)') is not None)
        self.assertTrue(autocode_line.parse('line','(v1 = 5.0') is not None)






