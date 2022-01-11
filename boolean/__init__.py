from typing import Dict

from boolean.cnf import CNF
from boolean.lex import Parser

def saturate(cnf: CNF) -> CNF:
    cur_clause_index = 1
    while cur_clause_index < len(cnf.clauses):
        cur_clause = cnf.clauses[cur_clause_index]
        curent_literals = cur_clause.literals
        for clause in cnf.clauses[:cur_clause_index]:
            for literal in clause.literals:
                if literal.negative() in curent_literals:
                    new_clause = cur_clause & clause
                    if new_clause is None:
                        return CNF()
                    cnf.add_clause(cur_clause & clause)
        cur_clause_index += 1
    return cnf

def is_satisfiable(formula: str) -> bool:
    clauses = Parser().parse_line(formula)
    cnf = CNF(*clauses)
    print(cnf)
    return saturate(cnf) != CNF()

def sat_assignment(formula: str) -> Dict[str, bool]:
    clauses = Parser().parse_line(formula)
    cnf = CNF(*clauses)

    unused_variables = set()
    assignment = dict()
    for clause in cnf.clauses:
        for literal in clause.literals:
            unused_variables.add(literal.variable)

    while len(unused_variables) != 0 and len(cnf.clauses) != 0:
        cnf = saturate(cnf)

        is_assignment_found = False
        for clause in cnf.clauses:
            if len(clause.literals) == 1:
                is_assignment_found = True
                literal = tuple(clause.literals)[0]
                assignment[literal.variable] = not literal.add_negation
                unused_variables.remove(literal.variable)
        if not is_assignment_found:
            variable = unused_variables.pop()
            assignment[variable] = False

        cnf.add_assignment(assignment)

    for variable in unused_variables:
        assignment[variable] = False
    return assignment

