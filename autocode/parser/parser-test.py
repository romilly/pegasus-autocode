import unittest
from autocode.parser import autocode_line


class ParserTest(unittest.TestCase):
    def try_to_parse(self, statement):
        self.assertTrue(autocode_line.parse('line',statement) is not None, 'cannot parse %s' % statement)

    def test_parses_tape_statements(self):
        self.try_to_parse('TAPE') 
        self.try_to_parse('n7 = TAPE') 
        self.try_to_parse('n7 = TAPE n2') 
        self.try_to_parse('n7 = TAPE *') 
        self.try_to_parse('v3 = TAPE') 
        self.try_to_parse('v3 = TAPE n2') 
        self.try_to_parse('v3 = TAPE *') 
        self.try_to_parse('n7 = TAPEB') 

    def test_parses_index_assignments(self):
        self.try_to_parse('n1 = 5') 
        self.try_to_parse('n1 = -5') 
        self.try_to_parse('n1 = n2') 
        self.try_to_parse('n1 = n2 + 5') 
        self.try_to_parse('n1 = n2 - 5') 
        self.try_to_parse('n1 = n2 x 5') 
        self.try_to_parse('n1 = n2 * 5') 
        self.try_to_parse('n1 = n2 + n7') 

    def test_parses_print_statements(self):
        self.try_to_parse('PRINT v7, 4000') 
        self.try_to_parse('PRINT n3, 4000') 
        self.try_to_parse('PRINT v7, n3') 
        self.try_to_parse('PRINT vn7, 3236') 

    def test_parses_variable_assignments(self):
        self.try_to_parse('v1 = 5.0')
        self.try_to_parse('v1 = -5.0') 
        self.try_to_parse('v1 = 5') 
        self.try_to_parse('v1 = v3') 
        self.try_to_parse('v1 = v3 + 5') 
        self.try_to_parse('v1 = v3 + 5') 
        self.try_to_parse('v1 = v3 x 5.0')
        self.try_to_parse('v1 = v3 / v2')

    def test_parses_mixed_assignments(self):
        self.try_to_parse('n1 = v2')
        self.try_to_parse('n1 = -v2')
        self.try_to_parse('v1 = n2')
        self.try_to_parse('v1 = n2 / n3')
        self.try_to_parse('v1 = 2/n3')
        self.try_to_parse('v1 = 2/3')
        self.try_to_parse('v1 = n2/3')


    def test_parses_modification(self):
        self.try_to_parse('vn7 = 323.6') 
        self.try_to_parse('v(5+n7) = 323.6') 
        self.try_to_parse('v(5+n7) = v(-7+n5) + v(3+n2)') 
        self.try_to_parse('vn7 = vn1 + 323.6') 
        self.try_to_parse('vn7 = vn1 + vn5') 

    def test_parses_functions(self):
        self.try_to_parse('v1 = MOD v2') 
        self.try_to_parse('v1 = -MOD v2') 
        self.try_to_parse('v1 = INT 5.6') 
        self.try_to_parse('v1 = INT v2') 
        self.try_to_parse('v1 = -INT v2') 
        self.try_to_parse('v1 = FRAC v2') 
        self.try_to_parse('v1 = SQRT v2') 
        self.try_to_parse('v1 = SIN v2') 
        self.try_to_parse('v1 = COS v2') 
        self.try_to_parse('v1 = TAN v2') 
        self.try_to_parse('v1 = CSC v2') 
        self.try_to_parse('v1 = SEC v2') 
        self.try_to_parse('v1 = COT v2') 
        self.try_to_parse('v1 = ARCSIN v2') 
        self.try_to_parse('v1 = ARCCOS v2') 
        self.try_to_parse('v1 = ARCTAN v2') 
        self.try_to_parse('v1 = LOG v2') 
        self.try_to_parse('v1 = EXP v2') 
        self.try_to_parse('v1 = EXPM v2') 
        self.try_to_parse('n1 = MOD n2') 
        self.try_to_parse('n1 = -MOD n2') 

    def test_parses_stop(self):
        self.try_to_parse('STOP') 

   # using ^ instead of ->

    def test_parses_jump_instructions(self):
        self.try_to_parse('^0') 
        self.try_to_parse('^n1') 
        self.try_to_parse('^0, v2 > v3') 
        self.try_to_parse('^0, v2 > 3.0') 
        self.try_to_parse('^0, -v2 > 3.0') 
        self.try_to_parse('^0, v2 >= 3.0')
        self.try_to_parse('^0, v2 /= 3.0')
        self.try_to_parse('^0, v2 /=* 3.0')
        self.try_to_parse('^0, v2 > -3.0')
        self.try_to_parse('^0, n2 > -3') 
        self.try_to_parse('^0, n2 = -3') 
        self.try_to_parse('^0, n2 = -3') 
        self.try_to_parse('^0, n2 = -3') 
        self.try_to_parse('^0, n2 = -3') 
        self.try_to_parse('^0, v1 =* v3') 
        self.try_to_parse('^(-4 +n8), v1 =* v3') 

    def test_processes_print_prefixes(self):
        self.try_to_parse('XP n1 = MOD n2') 
        self.try_to_parse('X n1 = MOD n2') 
        self.try_to_parse('SP n1 = MOD n2') 
        self.try_to_parse('S n1 = MOD n2') 

    def test_parses_bracketed_interludes(self):
        self.try_to_parse('(^0)') 
        self.try_to_parse('^0)') 
        self.try_to_parse('(v1 = 5.0') 






