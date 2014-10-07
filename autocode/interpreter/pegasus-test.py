import unittest
from autocode.ast.ast import *
from autocode.interpreter.pegasus import Pegasus




class PegasusTest(unittest.TestCase):
    def setUp(self):
        self.context = Pegasus()
        self.context.set('n1', 0)


    def test_can_access_indices(self):
        self.assertEquals(self.context.get('n1'), 0)
        expression = IndexAssignment(Index('n1'), Integer(5))
        expression.execute_in(self.context)
        self.assertEquals(self.context.get('n1'), 5)

