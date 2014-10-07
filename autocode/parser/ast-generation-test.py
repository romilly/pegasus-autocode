import unittest
from autocode.parser import autocode_line
from autocode.parser.ast import *


class AstGenerationTest(unittest.TestCase):
    def check(self, rule, text, expected):
         self.assertEqual(autocode_line.parse(rule, text),expected)

    def test_generates_integers(self):
        self.check('integer','37',Integer(37))

    def test_generates_indices(self):
        self.check('index','n5', Index('n5'))

    def test_generates_modifier(self):
        self.check('modifier','(5 + n2)', Modifier(Integer(5), Index('n2')))
        self.check('modifier','(-5 + n2)', Modifier(Negated(Integer(5)), Index('n2')))

    def test_generates_index_assignment(self):
        self.check('index_assignment', 'n1 = 5', IndexAssignment(Index('n1'), Integer(5)))
        self.check('index_assignment', 'n1 = -5', IndexAssignment(Index('n1'), Negated(Integer(5))))
        self.check('index_assignment', 'n1 = n2', IndexAssignment(Index('n1'), Index('n2')))
        self.check('index_assignment', 'n1 = n2 + 5', IndexAssignment(Index('n1'), Plus(Index('n2'), Integer(5))))
        self.check('index_assignment', 'n1 = n2 - 5', IndexAssignment(Index('n1'), Minus(Index('n2'), Integer(5))))
        self.check('index_assignment', 'n1 = n2 x 5', IndexAssignment(Index('n1'), Times(Index('n2'), Integer(5))))
        self.check('index_assignment', 'n1 = n2 * 5', IndexAssignment(Index('n1'), Remainder(Index('n2'), Integer(5))))
        self.check('index_assignment', 'n1 = n2 + n7',IndexAssignment(Index('n1'), Plus(Index('n2'), Index('n7'))))

    def test_generates_tape_statement(self):
        self.check('tape_statement','TAPE', ReadProgramTape())

    def test_generates_tape_reads(self):
        self.check('index_assignment','n7 = TAPE', MultipleIndexAssignment(Index('n7'), ReadDataTape('', 'TAPE')))
        self.check('index_assignment','n7 = TAPE n2', MultipleIndexAssignment(Index('n7'), ReadDataTape(Index('n2'), 'TAPE')))
        self.check('index_assignment','n7 = TAPE *', MultipleIndexAssignment(Index('n7'), ReadDataTape(MaxInt(), 'TAPE')))
        self.check('index_assignment','n7 = TAPEB', MultipleIndexAssignment(Index('n7'), ReadDataTape('', 'TAPEB')))
        # self.check('index_assignment','v3 = TAPE')
        # self.check('index_assignment','v3 = TAPE n2')
        # self.check('index_assignment','v3 = TAPE *')


