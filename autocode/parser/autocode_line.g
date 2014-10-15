from autocode.ast.ast import *
from autocode.ast.functions import *
from autocode.ast.printing import Print

%%

parser AutocodeLineParser:
    ignore: '\s'
    token EOL: '$'
    token INDEX: '[0-9][0-9]?'
    token mod: 'MOD'
    token function: 'MOD|INT|FRAC|SQRT|SIN|COS|TAN|CSC|SEC|COT|ARCSIN|ARCCOS|ARCTAN|LOG|EXPM|EXP'
    token special_printing: 'XP|X|SP|S'
    token prt: 'PRINT'
    token tapes: 'TAPE[B]?'
    token tape: 'TAPE'
    token spec: '[0-9]{4}'
    token label: '[1-9][0-9]?\)'
    token negate: '-'
    token op3: '\+|-|x'
    token div: '/'
    token plus: '\+'
    token FLOAT: '[0-9]*\.[0-9]+'
    token INT: '[0-9]{1,4}'
    token gets: '='
    token star: '\*'
    token lparen: '\('
    token rparen: '\)'
    token goto: '\^'
    token stop: 'STOP'
    token compare: '>=|>|/=\*|/=|=\*|='
    token icompare: '>=|>|/=|='
    rule line:
      [lparen]  [special_printing]
        [label]
        statement [rparen] EOL {{ return 'OK' }}
    rule op: ( op3 {{ return op3 }} | div {{ return div }} )
    rule statement: ( assignment {{ return assignment }} | print_statement {{ return print_statement }} |
        tape_statement  {{ return tape_statement }} | stop {{ return Stop() }} | jump {{ return jump }} )
    rule print_statement: prt (  index {{ source = index }}  | variable {{ source = variable }} )
            ',' ( spec {{ format = Integer(spec) }} | index {{ format = index }} )
            {{ return Print(source, format) }}
    rule tape_statement: tape {{ return ReadProgramTape() }}                                 # autocode manual sec 3.11
    rule assignment: index_assignment |  variable_assignment
    rule variable: 'v' variable_selector {{ return Variable(variable_selector) }}
    rule variable_selector:   ( integer {{ return integer }} | index {{ return index }} |
        modifier {{ return modifier }} )
    rule modifier: {{ neg = False }} lparen [negate {{neg = True }} ] integer plus index rparen
            {{ return Plus(integer if not neg else Negated(integer), index) }}
    rule index_assignment: index gets ( tape_spec {{ return MultipleIndexAssignment(index, tape_spec) }} |
        int_expression  {{ return IndexAssignment(index, int_expression) }} )
    rule variable_assignment: variable gets ( tape_spec {{ return MultipleVariableAssignment(variable, tape_spec) }} |
        var_expression {{ return VariableAssignment(variable, var_expression) }} )
    rule tape_spec: {{ qualifier = '' }} tapes [tape_qualifier {{ qualifier = tape_qualifier }} ]
            {{ return ReadDataTape(qualifier, tapes) }}
    rule tape_qualifier: ( index {{ return index }}  | star {{ return MaxInt() }} )
    rule var_expression:
        {{  neg = False }} [negate {{ neg=True }} ] var_negatable
        {{ return Negated(var_negatable) if neg else var_negatable }}
    rule var_negatable:  ( int_val  {{ has_div = False; i = int_val }} [ div int_val {{ has_div = True }} ]
        {{ return Div(i, int_val) if has_div else i }} |
         {{ is_op = False }} variable [ op var_val {{ is_op = True}} ]
       {{ return operation(op, variable, var_val) if is_op else variable }} |
        | float {{ return float }} | function var_val {{ return fun(function, var_val) }} )
    rule int_val: index {{ return index }} | integer {{ return integer }}
    rule var_val: variable {{ return variable }} | float {{ return float}} | integer {{return integer }}
    rule float_val: variable {{ return variable }} | float {{ return float }}
    rule int_expression: {{ is_op = False }} index [iop int_val {{ is_op = True}} ]
        {{ return ioperation(iop, index, int_val) if is_op else index }} |
        {{ is_negated = False }} [negate {{ is_negated = True }}] int_negatable
            {{ return Negated(int_negatable) if is_negated else int_negatable }}
    rule int_negatable:  ( integer {{ return integer }} | mod iv {{ return Mod(iv) }} |
        variable  {{ return variable }} )
    rule iv: ( index {{ return index }} | variable {{ return variable }} )
    rule iop: op3 {{ return op3 }} | star {{ return star }}
    rule jump: {{ is_conditional = False }} goto j_target [',' condition {{ is_conditional = True }} ]
        {{ return CJump(j_target, condition) if is_conditional else Jump(j_target) }}
    rule j_target: ( int_val {{ return int_val }} | modifier {{ return modifier }} )
    rule condition: {{ neg_1 = False; neg_2 = False }}
        [negate {{ neg_1 = True; neg_2 = False }} ] ( float_val {{ fv1 = float_val }} compare [negate {{ neg_2 = True }} ]
            float_val {{ return comparison(compare, (Negated(fv1) if neg_1 else fv1), (Negated(float_val) if neg_2 else float_val)) }}  |
        int_val icompare [negate] int_val)
    rule float: FLOAT {{ return Float(FLOAT) }}
    rule integer: INT {{ return Integer(INT) }}
    rule index: 'n' INDEX {{ return Index(INDEX) }}
