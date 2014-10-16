import unittest
from autocode.interpreter.ast import Float, Integer
from autocode.interpreter.printing import Print


class MockContext():
    def __init__(self):
        self.text = ''

    def write(self, text):
        self.text = text


class PrintTest(unittest.TestCase):
    def test_leading_1_or_3_formats_on_new_line(self):
        pr = Print(Float(2.718281),Integer(3026))
        dummy_context = MockContext()
        pr.evaluate_in(dummy_context)
        self.assertEquals(dummy_context.text, ' +2.718281')
