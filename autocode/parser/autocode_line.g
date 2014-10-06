from ast import Integer, Index, Modifier, IndexAssignment, Negated, operation

%%

parser AutocodeLineParser:
    ignore: '\s'
    token EOL: '$'
    token INDEX: 'n[0-9][0-9]?'
    token mod: 'MOD'
    token function: 'MOD|INT|FRAC|SQRT|SIN|COS|TAN|CSC|SEC|COT|ARCSIN|ARCCOS|ARCTAN|LOG|EXPM|EXP'
    token special_printing: 'XP|X|SP|S'
    token prt: 'PRINT'
    token tapes: 'TAPE[B]?'
    token tape: 'TAPE'
    token spec: '[0-9]{4}'
    token label: '[1-9][0-9]?\)'
    token negate: '-'
    token div: '/'
    token op: '\+|-|x|/'
    token plus: '\+'
    token float: '[0-9]*\.[0-9]*'
    token INT: '[0-9]{1,4}'
    token gets: '='
    token star: '\*'
    token lparen: '\('
    token rparen: '\)'
    token goto: '\^'
    token stop: 'STOP'
    token compare: '>=|>|\\=\*|\\=|=\*|='
    rule line:
      [lparen]  [special_printing] (
        label statement |
        statement ) [rparen] EOL {{ return 'OK' }}
    rule statement: ( assignment | print_statement | tape_statement | stop | jump )
    rule print_statement: prt ( index | variable ) ',' ( spec | index)
    rule tape_statement: tape                                              # autocode manual sec 3.11
    rule assignment: index_assignment |  var_assignment
    rule variable: 'v' variable_selector
    rule variable_selector:   ( integer {{ return integer }} | index {{ return index }} |
        modifier {{ return modifier }} )
    rule modifier: {{ neg = False }} lparen [negate {{neg = True }} ] integer plus index rparen
            {{ return Modifier(integer if not neg else Negated(integer), index) }}
    rule index_assignment: index gets ( tape_spec |
        int_expression  {{ return IndexAssignment(index, int_expression) }} )
    rule var_assignment: variable gets ( tape_spec | var_expression )
    rule tape_spec: tapes [tape_qualifier]
    rule tape_qualifier: ( index | star )
    rule var_expression: variable [var_tail] | [negate] ( int_val [ div int_val ] | float | function var_val )
    rule int_val: index {{ return index }} | integer {{ return integer }}
    rule var_tail: op ( integer | float | variable)
    rule var_val: variable | float
    rule int_expression: {{ is_op = False }} index [iop int_val {{ is_op = True}} ]
        {{ return operation(iop, index, int_val) if is_op else index }} |
        {{ is_negated = False }} [negate {{ is_negated = True }}] int_negatable
            {{ return Negated(int_negatable) if is_negated else int_negatable }}
    rule int_negatable:  ( integer {{ return integer }} | mod ( variable | index ) | variable)
    rule iop: op {{ return op }}| star {{ return star }}
    rule jump: goto ( int_val | modifier) [',' condition]
    rule condition: [negate] ( (var_val compare [negate] var_val ) | ( int_val compare [negate] int_val) )
    rule integer: INT {{ return Integer(INT) }}
    rule index: INDEX {{ return Index(INDEX) }}
