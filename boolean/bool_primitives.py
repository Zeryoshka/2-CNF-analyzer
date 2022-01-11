from typing import List
from dataclasses import dataclass

@dataclass
class Literal:
    variable: str
    add_negation: bool

    def negative(self):
        return Literal(self.variable, not self.add_negation)

    def __hash__(self):
        return hash(self.variable) + hash(self.add_negation)

    def __str__(self):
        head = '~' if self.add_negation else ''
        return head + self.variable

    def __eq__(self, other):
        return self.variable == other.variable and \
            self.add_negation == other.add_negation

class Clause:
    def __init__(self, *literals):
        self._literals = frozenset(literals)

    @property
    def literals(self):
        return self._literals

    def __str__(self):
        if len(self.literals) == 0:
            return '1'
        return '(' + '\\/'.join(map(str, self.literals)) + ')'

    def __eq__(self, other):
        return self._literals == other._literals

    def __and__(self, other):
        literals = set(self.literals)
        is_one_removed = False
        for new_literal in set(other.literals):
            if new_literal in literals:
                continue
            if new_literal.negative() in literals:
                if not is_one_removed:
                    literals.remove(new_literal.negative())
                    is_one_removed = True
                else:
                    return Clause()
            else:
                literals.add(new_literal)
        if len(literals) == 0:
            return None
        return Clause(*literals)

    def __hash__(self):
        return hash(frozenset)

class ParserCNF:
    def __init__(self, *clauses):
        self.clauses = list(clauses)

    def linearized_clauses(self) -> List[Clause]:
        clauses = []
        for clause in self.clauses:
            if type(clause) == ParserCNF:
                clauses += clause.linearized_clauses()
            else:
                clauses.append(clause)
        return clauses
