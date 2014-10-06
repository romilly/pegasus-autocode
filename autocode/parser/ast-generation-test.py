import unittest
from autocode.parser import autocode_line
from autocode.parser.ast import Integer, Index, Modifier, IndexAssignment, Plus, Negated


class AstGenerationTest(unittest.TestCase):
    def test_generates_integers(self):
        self.assertEqual(autocode_line.parse('integer','37'), Integer(37))

    def test_generates_indices(self):
        self.assertEqual(autocode_line.parse('index','n5'), Index('n5'))

    def test_generates_modifier(self):
        self.assertEqual(autocode_line.parse('modifier','(5 + n2)'), Modifier(Integer(5), Index('n2')))
        self.assertEqual(autocode_line.parse('modifier','(-5 + n2)'), Modifier(Negated(Integer(5)), Index('n2')))

    def test_generates_int_assignment(self):
        self.assertEqual(autocode_line.parse('index_assignment', 'n1 = 5'), IndexAssignment(Index('n1'), Integer(5)))
        self.assertEqual(autocode_line.parse('index_assignment', 'n1 = -5'), IndexAssignment(Index('n1'), Negated(Integer(5))))
        self.assertEqual(autocode_line.parse('index_assignment', 'n1 = n2'), IndexAssignment(Index('n1'), Index('n2')))
        self.assertEqual(autocode_line.parse('index_assignment', 'n1 = n2 + 5'), IndexAssignment(Index('n1'), Plus(Index('n2'), Integer(5))))


