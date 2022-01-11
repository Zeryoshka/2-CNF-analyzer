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


class Clause:
    def __init__(self, *literals):
        self._literals = frozenset(literals)

    @property
    def literals(self):
        return self._literals

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
