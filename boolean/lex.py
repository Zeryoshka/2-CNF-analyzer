from ply.lex import lex
from ply.yacc import yacc

from bool_primitives import Literal, Clause, ParserCNF

class Parser:
    tokens = (
        'VAR',
        'LBRACKET',
        'RBRACKET',
        'NEGATION',
        'CONJUNCTION',
        'DISJUNCTION',
        'IMPLICATION'
    )

    t_VAR = r'[a-z]'
    t_LBRACKET = r'\('
    t_RBRACKET = r'\)'
    t_NEGATION = r'\~'
    t_CONJUNCTION = r'/\\'
    t_DISJUNCTION = r'\\/'
    t_IMPLICATION  = r'->'

    t_ignore  = ' '

    def p_cnf(self, p):
        '''cnf : clause CONJUNCTION cnf
               | clause
        '''
        if len(p) == 2:
            p[0] = ParserCNF(p[1])
        else:
            p[0] = ParserCNF(p[1], p[3])

    def p_clause(self, p):
        '''clause : LBRACKET literal DISJUNCTION literal RBRACKET
                  | LBRACKET literal IMPLICATION literal RBRACKET'''
        if p[2] == '->':
            p[0] = Clause(p[2].negative(), p[4])
        else:
            p[0] = Clause(p[2], p[4])

    def p_literal(self, p):
        '''literal : NEGATION VAR
                   | VAR'''
        if p[1] == '~':
            p[0] = Literal(p[2], True)
        else:
            p[0] = Literal(p[1], False)

    def __init__(self):
        self.lexer = lex(module=self)
        self.parser = yacc(module=self)

    def parse_line(self, s: str):
        result: ParserCNF = self.parser.parse(s)
        return result.linearized_clauses()
