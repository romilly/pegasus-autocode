# ast code will be imported here

%%

parser AutocodeLineParser:
    ignore: '\s'
    token EOL: '$'
    token index: 'n[0-9][0-9]?'
    token mod: 'MOD'
    token function: 'MOD|INT|FRAC|SQRT|SIN|COS|TAN|CSC|SEC|COT|ARCSIN|ARCCOS|ARCTAN|LOG|EXPM|EXP'
    token plus: '\+'
    token var: 'v'
    token prt: 'PRINT'
    token tape: 'TAPE'
    token spec: '[0-9]{4}'
    token label: '[1-9][0-9]?\)'
    token directive: 'D|T'
    token negate: '-'
    token div: '/'
    token op: '\+|-|x|/'
    token integer: '[0-9]{1,4}'
    token float: '[0-9]*\.[0-9]*'
    token gets: '='
    token star: '\*'
    token lparen: '\('
    token rparen: '\)'
    token goto: '\^'
    token stop: 'STOP'
    token compare: '>=|>|\\=\*|\\=|=\*|='
    rule line:
        ( directive |
        label statement |
        statement ) EOL {{ return 'OK' }}
    rule statement: ( assignment | print_statement | tape_statement | stop | jump )
    rule print_statement: prt ( index | variable ) ',' ( spec | index)
    rule tape_statement: tape                                              # autocode manual sec 3.11
    rule assignment: int_assignment |  var_assignment
    rule variable: var ( integer | index | modifier)
    rule modifier: lparen [negate] integer plus index rparen
    rule int_assignment: index gets ( tape_spec | int_expression )
    rule var_assignment: variable gets ( tape_spec | var_expression )
    rule tape_spec: tape [tape_qualifier]
    rule tape_qualifier: ( index | star )
    rule var_expression: variable [var_tail] | [negate] ( int_val [ div int_val ] | float | function var_val )
    rule int_val: index | integer
    rule var_tail: op ( integer | float | variable)
    rule var_val: variable | float
    rule int_expression: index [int_tail] | [negate] ( integer | mod ( variable | index ) | variable)
    rule int_op: op | star
    rule int_tail: int_op (index | integer)
    rule jump: goto ( int_val | modifier) [',' condition]
    rule condition: [negate] (var_val | int_val) compare [negate] (var_val | int_val)
