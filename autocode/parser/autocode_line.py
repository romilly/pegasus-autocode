from autocode.ast.ast import *
from autocode.ast.functions import *
from autocode.ast.printing import Print


# Begin -- grammar generated by Yapps
import sys, re
from yapps import runtime

class AutocodeLineParserScanner(runtime.Scanner):
    patterns = [
        ("'v'", re.compile('v')),
        ("','", re.compile(',')),
        ('\\s', re.compile('\\s')),
        ('EOL', re.compile('$')),
        ('INDEX', re.compile('n[0-9][0-9]?')),
        ('mod', re.compile('MOD')),
        ('function', re.compile('MOD|INT|FRAC|SQRT|SIN|COS|TAN|CSC|SEC|COT|ARCSIN|ARCCOS|ARCTAN|LOG|EXPM|EXP')),
        ('special_printing', re.compile('XP|X|SP|S')),
        ('prt', re.compile('PRINT')),
        ('tapes', re.compile('TAPE[B]?')),
        ('tape', re.compile('TAPE')),
        ('spec', re.compile('[0-9]{4}')),
        ('label', re.compile('[1-9][0-9]?\\)')),
        ('negate', re.compile('-')),
        ('op3', re.compile('\\+|-|x')),
        ('div', re.compile('/')),
        ('plus', re.compile('\\+')),
        ('FLOAT', re.compile('[0-9]*\\.[0-9]+')),
        ('INT', re.compile('[0-9]{1,4}')),
        ('gets', re.compile('=')),
        ('star', re.compile('\\*')),
        ('lparen', re.compile('\\(')),
        ('rparen', re.compile('\\)')),
        ('goto', re.compile('\\^')),
        ('stop', re.compile('STOP')),
        ('compare', re.compile('>=|>|/=\\*|/=|=\\*|=')),
        ('icompare', re.compile('>=|>|/=|=')),
    ]
    def __init__(self, str,*args,**kw):
        runtime.Scanner.__init__(self,None,{'\\s':None,},str,*args,**kw)

class AutocodeLineParser(runtime.Parser):
    Context = runtime.Context
    def line(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'line', [])
        if self._peek('lparen', 'special_printing', 'label', 'stop', 'prt', 'tape', 'goto', "'v'", 'INDEX', context=_context) == 'lparen':
            lparen = self._scan('lparen', context=_context)
        if self._peek('special_printing', 'label', 'stop', 'prt', 'tape', 'goto', "'v'", 'INDEX', context=_context) == 'special_printing':
            special_printing = self._scan('special_printing', context=_context)
        if self._peek('label', 'stop', 'prt', 'tape', 'goto', "'v'", 'INDEX', context=_context) == 'label':
            label = self._scan('label', context=_context)
        statement = self.statement(_context)
        if self._peek('rparen', 'EOL', context=_context) == 'rparen':
            rparen = self._scan('rparen', context=_context)
        EOL = self._scan('EOL', context=_context)
        return 'OK'

    def op(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'op', [])
        _token = self._peek('op3', 'div', context=_context)
        if _token == 'op3':
            op3 = self._scan('op3', context=_context)
            return op3
        else: # == 'div'
            div = self._scan('div', context=_context)
            return div

    def statement(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'statement', [])
        _token = self._peek('stop', 'prt', 'tape', 'goto', "'v'", 'INDEX', context=_context)
        if _token in ["'v'", 'INDEX']:
            assignment = self.assignment(_context)
            return assignment
        elif _token == 'prt':
            print_statement = self.print_statement(_context)
            return print_statement
        elif _token == 'tape':
            tape_statement = self.tape_statement(_context)
            return tape_statement
        elif _token == 'stop':
            stop = self._scan('stop', context=_context)
            return Stop()
        else: # == 'goto'
            jump = self.jump(_context)
            return jump

    def print_statement(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'print_statement', [])
        prt = self._scan('prt', context=_context)
        _token = self._peek('INDEX', "'v'", context=_context)
        if _token == 'INDEX':
            index = self.index(_context)
            source = index
        else: # == "'v'"
            variable = self.variable(_context)
            source = variable
        self._scan("','", context=_context)
        _token = self._peek('spec', 'INDEX', context=_context)
        if _token == 'spec':
            spec = self._scan('spec', context=_context)
            format = Integer(spec)
        else: # == 'INDEX'
            index = self.index(_context)
            format = index
        return Print(source, format)

    def tape_statement(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'tape_statement', [])
        tape = self._scan('tape', context=_context)
        return ReadProgramTape()

    def assignment(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'assignment', [])
        _token = self._peek("'v'", 'INDEX', context=_context)
        if _token == 'INDEX':
            index_assignment = self.index_assignment(_context)
        else: # == "'v'"
            variable_assignment = self.variable_assignment(_context)

    def variable(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'variable', [])
        self._scan("'v'", context=_context)
        variable_selector = self.variable_selector(_context)
        return Variable(variable_selector)

    def variable_selector(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'variable_selector', [])
        _token = self._peek('INT', 'INDEX', 'lparen', context=_context)
        if _token == 'INT':
            integer = self.integer(_context)
            return integer
        elif _token == 'INDEX':
            index = self.index(_context)
            return index
        else: # == 'lparen'
            modifier = self.modifier(_context)
            return modifier

    def modifier(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'modifier', [])
        neg = False
        lparen = self._scan('lparen', context=_context)
        if self._peek('negate', 'INT', context=_context) == 'negate':
            negate = self._scan('negate', context=_context)
            neg = True
        integer = self.integer(_context)
        plus = self._scan('plus', context=_context)
        index = self.index(_context)
        rparen = self._scan('rparen', context=_context)
        return Plus(integer if not neg else Negated(integer), index)

    def index_assignment(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'index_assignment', [])
        index = self.index(_context)
        gets = self._scan('gets', context=_context)
        _token = self._peek('tapes', 'negate', 'INDEX', 'mod', "'v'", 'INT', context=_context)
        if _token == 'tapes':
            tape_spec = self.tape_spec(_context)
            return MultipleIndexAssignment(index, tape_spec)
        else: # in ['negate', 'INDEX', 'mod', "'v'", 'INT']
            int_expression = self.int_expression(_context)
            return IndexAssignment(index, int_expression)

    def variable_assignment(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'variable_assignment', [])
        variable = self.variable(_context)
        gets = self._scan('gets', context=_context)
        _token = self._peek('tapes', 'negate', "'v'", 'function', 'FLOAT', 'INDEX', 'INT', 'rparen', 'EOL', context=_context)
        if _token == 'tapes':
            tape_spec = self.tape_spec(_context)
            return MultipleVariableAssignment(variable, tape_spec)
        else:
            var_expression = self.var_expression(_context)
            return VariableAssignment(variable, var_expression)

    def tape_spec(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'tape_spec', [])
        qualifier = ''
        tapes = self._scan('tapes', context=_context)
        if self._peek('star', 'INDEX', 'rparen', 'EOL', context=_context) in ['star', 'INDEX']:
            tape_qualifier = self.tape_qualifier(_context)
            qualifier = tape_qualifier
        return ReadDataTape(qualifier, tapes)

    def tape_qualifier(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'tape_qualifier', [])
        _token = self._peek('star', 'INDEX', context=_context)
        if _token == 'INDEX':
            index = self.index(_context)
            return index
        else: # == 'star'
            star = self._scan('star', context=_context)
            return MaxInt()

    def var_expression(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'var_expression', [])
        neg = False
        if self._peek('negate', "'v'", 'function', 'FLOAT', 'INDEX', 'INT', 'rparen', 'EOL', context=_context) == 'negate':
            negate = self._scan('negate', context=_context)
            neg=True
        var_negatable = self.var_negatable(_context)
        return Negated(var_negatable) if neg else var_negatable

    def var_negatable(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'var_negatable', [])
        _token = self._peek("'v'", 'function', 'FLOAT', 'INDEX', 'INT', 'rparen', 'EOL', context=_context)
        if _token in ['INDEX', 'INT']:
            int_val = self.int_val(_context)
            has_div = False; i = int_val
            if self._peek('div', 'rparen', 'EOL', context=_context) == 'div':
                div = self._scan('div', context=_context)
                int_val = self.int_val(_context)
                has_div = True
            return Div(i, int_val) if has_div else i
        elif _token == "'v'":
            is_op = False
            variable = self.variable(_context)
            if self._peek('op3', 'div', 'rparen', 'EOL', context=_context) in ['op3', 'div']:
                op = self.op(_context)
                var_val = self.var_val(_context)
                is_op = True
            return operation(op, variable, var_val) if is_op else variable
        elif _token not in ['function', 'FLOAT']:
            pass
        elif _token == 'FLOAT':
            float = self.float(_context)
            return float
        else: # == 'function'
            function = self._scan('function', context=_context)
            var_val = self.var_val(_context)
            return fun(function, var_val)

    def int_val(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'int_val', [])
        _token = self._peek('INDEX', 'INT', context=_context)
        if _token == 'INDEX':
            index = self.index(_context)
            return index
        else: # == 'INT'
            integer = self.integer(_context)
            return integer

    def var_val(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'var_val', [])
        _token = self._peek("'v'", 'FLOAT', 'INT', context=_context)
        if _token == "'v'":
            variable = self.variable(_context)
            return variable
        elif _token == 'FLOAT':
            float = self.float(_context)
            return float
        else: # == 'INT'
            integer = self.integer(_context)
            return integer

    def float_val(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'float_val', [])
        _token = self._peek("'v'", 'FLOAT', context=_context)
        if _token == "'v'":
            variable = self.variable(_context)
            return variable
        else: # == 'FLOAT'
            float = self.float(_context)
            return float

    def int_expression(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'int_expression', [])
        _token = self._peek('negate', 'INDEX', 'mod', "'v'", 'INT', context=_context)
        if _token == 'INDEX':
            is_op = False
            index = self.index(_context)
            if self._peek('op3', 'star', 'rparen', 'EOL', context=_context) in ['op3', 'star']:
                iop = self.iop(_context)
                int_val = self.int_val(_context)
                is_op = True
            return ioperation(iop, index, int_val) if is_op else index
        else: # in ['negate', 'mod', "'v'", 'INT']
            is_negated = False
            if self._peek('negate', 'mod', "'v'", 'INT', context=_context) == 'negate':
                negate = self._scan('negate', context=_context)
                is_negated = True
            int_negatable = self.int_negatable(_context)
            return Negated(int_negatable) if is_negated else int_negatable

    def int_negatable(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'int_negatable', [])
        _token = self._peek('mod', "'v'", 'INT', context=_context)
        if _token == 'INT':
            integer = self.integer(_context)
            return integer
        elif _token == 'mod':
            mod = self._scan('mod', context=_context)
            iv = self.iv(_context)
            return Mod(iv)
        else: # == "'v'"
            variable = self.variable(_context)
            return variable

    def iv(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'iv', [])
        _token = self._peek("'v'", 'INDEX', context=_context)
        if _token == 'INDEX':
            index = self.index(_context)
            return index
        else: # == "'v'"
            variable = self.variable(_context)
            return variable

    def iop(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'iop', [])
        _token = self._peek('op3', 'star', context=_context)
        if _token == 'op3':
            op3 = self._scan('op3', context=_context)
            return op3
        else: # == 'star'
            star = self._scan('star', context=_context)
            return star

    def jump(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'jump', [])
        is_conditional = False
        goto = self._scan('goto', context=_context)
        j_target = self.j_target(_context)
        if self._peek("','", 'rparen', 'EOL', context=_context) == "','":
            self._scan("','", context=_context)
            condition = self.condition(_context)
            is_conditional = True
        return CJump(j_target, condition) if is_conditional else Jump(j_target)

    def j_target(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'j_target', [])
        _token = self._peek('lparen', 'INDEX', 'INT', context=_context)
        if _token != 'lparen':
            int_val = self.int_val(_context)
            return int_val
        else: # == 'lparen'
            modifier = self.modifier(_context)
            return modifier

    def condition(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'condition', [])
        neg_1 = False; neg_2 = False
        if self._peek('negate', "'v'", 'FLOAT', 'INDEX', 'INT', context=_context) == 'negate':
            negate = self._scan('negate', context=_context)
            neg_1 = True; neg_2 = False
        _token = self._peek("'v'", 'FLOAT', 'INDEX', 'INT', context=_context)
        if _token not in ['INDEX', 'INT']:
            float_val = self.float_val(_context)
            fv1 = float_val
            compare = self._scan('compare', context=_context)
            if self._peek('negate', "'v'", 'FLOAT', context=_context) == 'negate':
                negate = self._scan('negate', context=_context)
                neg_2 = True
            float_val = self.float_val(_context)
            return comparison(compare, (Negated(fv1) if neg_1 else fv1), (Negated(float_val) if neg_2 else float_val))
        else: # in ['INDEX', 'INT']
            int_val = self.int_val(_context)
            icompare = self._scan('icompare', context=_context)
            if self._peek('negate', 'INDEX', 'INT', context=_context) == 'negate':
                negate = self._scan('negate', context=_context)
            int_val = self.int_val(_context)

    def float(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'float', [])
        FLOAT = self._scan('FLOAT', context=_context)
        return Float(FLOAT)

    def integer(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'integer', [])
        INT = self._scan('INT', context=_context)
        return Integer(INT)

    def index(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'index', [])
        INDEX = self._scan('INDEX', context=_context)
        return Index(INDEX)


def parse(rule, text):
    P = AutocodeLineParser(AutocodeLineParserScanner(text))
    return runtime.wrap_error_reporter(P, rule)

if __name__ == '__main__':
    from sys import argv, stdin
    if len(argv) >= 2:
        if len(argv) >= 3:
            f = open(argv[2],'r')
        else:
            f = stdin
        print parse(argv[1], f.read())
    else: print >>sys.stderr, 'Args:  <rule> [<filename>]'
# End -- grammar generated by Yapps
