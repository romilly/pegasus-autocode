import unittest
from autocode.ast.printing import Print
from autocode.parser import autocode_line
from autocode.ast.ast import *
from autocode.ast.functions import *


class AstGenerationTest(unittest.TestCase):
    def check(self, rule, text, expected):
         self.assertEqual(autocode_line.parse(rule, text),expected)

    def test_generates_tape_statement(self):
        self.check('tape_statement','TAPE', ReadProgramTape())

    def test_generates_tape_reads(self):
        self.check('index_assignment','n7 = TAPE', MultipleIndexAssignment(Index('n7'), ReadDataTape('', 'TAPE')))
        self.check('index_assignment','n7 = TAPE n2',
                   MultipleIndexAssignment(Index('n7'), ReadDataTape(Index('n2'), 'TAPE')))
        self.check('index_assignment','n7 = TAPE *', MultipleIndexAssignment(Index('n7'),
                   ReadDataTape(MaxInt(), 'TAPE')))
        self.check('index_assignment','n7 = TAPEB', MultipleIndexAssignment(Index('n7'), ReadDataTape('', 'TAPEB')))
        self.check('variable_assignment','v3 = TAPE',
                   MultipleVariableAssignment(Variable(Integer(3)), ReadDataTape('','TAPE')))
        self.check('variable_assignment','v3 = TAPE n2',
                   MultipleVariableAssignment(Variable(Integer(3)), ReadDataTape(Index('n2'),'TAPE')))
        self.check('variable_assignment','v3 = TAPE *',
                   MultipleVariableAssignment(Variable(Integer(3)), ReadDataTape(MaxInt(),'TAPE')))

    def test_generates_index_assignment(self):
        self.check('index_assignment', 'n1 = 5', IndexAssignment(Index('n1'), Integer(5)))
        self.check('index_assignment', 'n1 = -5', IndexAssignment(Index('n1'), Negated(Integer(5))))
        self.check('index_assignment', 'n1 = n2', IndexAssignment(Index('n1'), Index('n2')))
        self.check('index_assignment', 'n1 = n2 + 5', IndexAssignment(Index('n1'), Plus(Index('n2'), Integer(5))))
        self.check('index_assignment', 'n1 = n2 - 5', IndexAssignment(Index('n1'), Minus(Index('n2'), Integer(5))))
        self.check('index_assignment', 'n1 = n2 x 5', IndexAssignment(Index('n1'), Times(Index('n2'), Integer(5))))
        self.check('index_assignment', 'n1 = n2 * 5', IndexAssignment(Index('n1'), Remainder(Index('n2'), Integer(5))))
        self.check('index_assignment', 'n1 = n2 + n7',IndexAssignment(Index('n1'), Plus(Index('n2'), Index('n7'))))

    def test_generates_print_statements(self):
        self.check('print_statement','PRINT v7, 3016', Print(Variable(Integer(7)),Integer(3016)))
        self.check('print_statement', 'PRINT n3, 4000', Print(Index('n3'), Integer(4000)))
        self.check('print_statement', 'PRINT v7, n3', Print(Variable(Integer(7)), Index('n3')))
        self.check('print_statement', 'PRINT vn7, 3236', Print(Variable(Index('n7')), Integer(3236)))
        
    def test_generates_variable_assignments(self):
        self.check('variable_assignment','v1 = 5.0', VariableAssignment(Variable(Integer(1)), Float('5.0')))
        self.check('variable_assignment','v1 = -5.0', VariableAssignment(Variable(Integer(1)), Negated(Float('5.0'))))
        self.check('variable_assignment','v1 = 5', VariableAssignment(Variable(Integer(1)), Integer(5)))
        self.check('variable_assignment','v1 = v3', VariableAssignment(Variable(Integer(1)), Variable(Integer(3))))
        self.check('variable_assignment','v1 = v3 + 5', VariableAssignment(Variable(Integer(1)),
                Plus(Variable(Integer(3)), Integer(5))))
        self.check('variable_assignment','v1 = v3 - 5', VariableAssignment(Variable(Integer(1)),
                Minus(Variable(Integer(3)), Integer(5))))
        self.check('variable_assignment','v1 = v3 x 5.0', VariableAssignment(Variable(Integer(1)),
                Times(Variable(Integer(3)), Float(5.0))))
        self.check('variable_assignment','v1 = v3 / v2',
                   VariableAssignment(Variable(Integer(1)), Div(Variable(Integer(3)), Variable(Integer(2)))))
        
    def test_generates_mixed_assignments(self):
        self.check('index_assignment', 'n1 = v2', IndexAssignment(Index('n1'), Variable(Integer(2))))
        self.check('index_assignment', 'n1 = -v2', IndexAssignment(Index('n1'), Negated(Variable(Integer(2)))))
        self.check('variable_assignment', 'v1 = n2', VariableAssignment(Variable(Integer(1)), Index('n2')))
        self.check('variable_assignment', 'v1 = n2 / n3',
                   VariableAssignment(Variable(Integer(1)), Div(Index('n2'),Index('n3'))))
        self.check('variable_assignment', 'v1 = 2/n3',
                   VariableAssignment(Variable(Integer(1)), Div(Integer(2),Index('n3'))))
        self.check('variable_assignment', 'v1 = 2/3',
                    VariableAssignment(Variable(Integer(1)), Div(Integer(2),Integer(3))))
        self.check('variable_assignment', 'v1 = n2/3',
                    VariableAssignment(Variable(Integer(1)), Div(Index('n2'),Integer(3))))
        
    def test_generates_modification(self):
        self.check('variable_assignment','vn7 = 323.6',
                   VariableAssignment(Variable(Index('n7')),Float(323.6)))
        self.check('variable_assignment','v(5+n7) = 323.6',
                   VariableAssignment(Variable(Plus(Integer(5),Index('n7'))),Float(323.6)))
        self.check('variable_assignment','v(5+n7) = v(-7+n5) + v(3+n2)',
                   VariableAssignment(Variable(Plus(Integer(5),Index('n7'))),
                        Plus(Variable(Plus(Negated(Integer(7)), Index('n5'))),Variable(Plus(Integer(3),Index('n2'))))))
        
    def test_generates_functions(self):
        self.check('variable_assignment','v1 = MOD v2',
                   VariableAssignment(Variable(Integer(1)),Mod(Variable(Integer(2)))))
        self.check('variable_assignment','v1 = -MOD v2',
                   VariableAssignment(Variable(Integer(1)),Negated(Mod(Variable(Integer(2))))))
        self.check('variable_assignment','v1 = INT 5.6', VariableAssignment(Variable(Integer(1)), Int(Float(5.6))))
        self.check('variable_assignment','v1 = INT v2',
                   VariableAssignment(Variable(Integer(1)), Int(Variable(Integer(2)))))
        self.check('variable_assignment','v1 = -INT v2',
                   VariableAssignment(Variable(Integer(1)), Negated(Int(Variable(Integer(2))))))
        self.check('variable_assignment','v1 = FRAC v2',
                   VariableAssignment(Variable(Integer(1)), Frac(Variable(Integer(2)))))
        self.check('index_assignment','n1 = MOD n2', IndexAssignment(Index('n1'), Mod(Index('n2'))))
        self.check('index_assignment','n1 = -MOD n2',
                   IndexAssignment(Index('n1'), Negated(Mod(Index('n2')))))

    def test_generates_stop(self):
        self.check('statement','STOP', Stop())


    def test_generates_jumps(self):
        self.check('jump','^0', Jump(Integer(0)))
        self.check('jump','^n1', Jump(Index('n1')))
        self.check('jump','^0, v2 > v3', CJump(Integer(0), GT(Variable(Integer(2)), Variable(Integer(3)))))
        # self.try_to_parse('^0, v2 > 3.0')
        # self.try_to_parse('^0, -v2 > 3.0')
        # self.try_to_parse('^0, v2 > -3.0')
        # self.try_to_parse('^0, n2 > -3')
        # self.try_to_parse('^0, n2 = -3')
        # self.try_to_parse('^0, n2 = -3')
        # self.try_to_parse('^0, n2 = -3')
        # self.try_to_parse('^0, n2 = -3')
        # self.try_to_parse('^0, v1 =* v3')
        # self.try_to_parse('^(-4 +n8), v1 =* v3')

