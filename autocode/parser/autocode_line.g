# ast code will be imported here

%%

parser AutocodeLineParser:
    ignore: '\s'
    token EOL: '$'
    token index: 'n[0-9][0-9]?'
    token function: 'MOD'
    token plus: '\+'
    token var: 'v'
    token prt: 'PRINT'
    token tape: 'TAPE'
    token spec: '[0-9]{4}'
    token label: '[1-9][0-9]?\)'
    token directive: 'D|T'
    token op: '\+|-|x|/'
    token integer: '[0-9]{1,4}'
    token float: '[0-9]*\.[0-9]*'
    token end: '\^0'
    token gets: '='
    token negate: '-'
    token star: '\*'
    token lparen: '\('
    token rparen: '\)'
    rule line:
        ( directive |
        label statement |
        statement |
        end ) EOL {{ return 'OK' }}
    rule statement: ( assignment | print_statement | tape_statement)
    rule print_statement: prt ( index | variable ) ',' ( spec | index)
    rule tape_statement: tape                                              # autocode manual sec 3.11
    rule assignment: int_assignment | var_assignment
    rule variable: var ( integer | index | modifier)
    rule modifier: lparen [negate] integer plus index rparen
    rule int_assignment: index gets ( tape_spec | int_expression)
    rule var_assignment: variable gets ( tape_spec | var_expression )
    rule tape_spec: tape [tape_qualifier]
    rule tape_qualifier: ( index | star )
    rule var_expression: [negate] float | variable [var_tail] | function ( float | variable)
    rule var_tail: op ( integer | float | variable)
    rule int_expression: [negate] integer | index [int_tail]
    rule int_op: op | star
    rule int_tail: int_op (index | integer)
