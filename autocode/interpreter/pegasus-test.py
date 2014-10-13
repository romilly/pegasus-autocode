import unittest
import cStringIO
from autocode.ast.ast import *
from autocode.ast.printing import Print
from autocode.ast.progam import Program, Line
from autocode.interpreter.pegasus import Pegasus


class PegasusTest(unittest.TestCase):
    def setUp(self):
        self.output = cStringIO.StringIO()

    # def test_can_run_a_program(self):
    #     program = Program(
    #         Line(VariableAssignment(Variable(Integer(1)), Float(3.0))),
    #         Line(Print(Variable(Integer(1)), Integer(4032))),
    #         Line(Stop())
    #     )
    #     Pegasus(self.output, program).run()
    #     self.assertEquals(self.output.getvalue(),'3.0')
    #


    def test_can_run_my_program(self):
        # v1 = 1.0
        # v2 = 1.0
        # v3 = 0.00001
        # v4 = 1.0
        # 1) ^2, v3 > v2
        # v2 = v2 / v4
        # v1 = v1 + v2
        # v4 = v4 + 1.0
        # ^1
        # 2) PRINT v1, 3026
        # STOP
        # (^0)
         program = Program(
            Line(VariableAssignment(Variable(Integer(1)), Float(1.0))),
            Line(VariableAssignment(Variable(Integer(2)), Float(1.0))),
            Line(VariableAssignment(Variable(Integer(3)), Float(0.00001))),
            Line(VariableAssignment(Variable(Integer(4)), Float(1.0))),
            Line(CJump(Integer(2), GT(Variable(Integer(3)), Variable(Integer(2)))), 1),
            Line(VariableAssignment(Variable(Integer(2)), Div(Variable(Integer(2)),Variable(Integer(4))))),
            Line(VariableAssignment(Variable(Integer(1)), Plus(Variable(Integer(1)),Variable(Integer(2))))),
            Line(VariableAssignment(Variable(Integer(4)), Plus(Variable(Integer(4)),Float(1.0)))),
            Line(Jump(Integer(1))),
            Line(Print(Variable(Integer(1)), Integer(3026)), 2),
            Line(Stop())
         )
         Pegasus(self.output, program).run()
         print self.output.getvalue()

