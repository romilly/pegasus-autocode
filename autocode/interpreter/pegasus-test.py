import unittest
import cStringIO
from autocode.ast.ast import *
from autocode.interpreter.pegasus import Pegasus


class PegasusTest(unittest.TestCase):
    def setUp(self):
        self.output = cStringIO.StringIO()
        self.context = Pegasus(self.output)
        self.context.set('n1', 0)
        self.context.set('n7', 3)
        self.context.set('v3', 12.5)

    def test_can_access_indices(self):
        self.assertEquals(self.context.get('n1'), 0)
        expression = IndexAssignment(Index('n1'), Integer(5))
        expression.evaluate_in(self.context)
        self.assertEquals(self.context.get('n1'), 5)

    def test_can_print(self):
        expression = Print(Variable(Index('n7')), Integer(3236))
        expression.evaluate_in(self.context)
        self.assertEquals(self.output.getvalue(), '12.5')


