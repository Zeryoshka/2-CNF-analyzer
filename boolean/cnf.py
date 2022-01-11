from boolean.bool_primitives import Clause

class CNF:
    def __init__(self, *clauses):
        self._clauses_set = set(clauses)
        self._clauses = list(self._clauses_set)

    @property
    def clauses(self):
        return self._clauses

    def add_clause(self, clause):
        if (
            (clause.literals is not None) and \
            (clause not in self._clauses_set) and \
            (clause != Clause())
        ):
            self._clauses.append(clause)
            self._clauses_set.add(clause)

    def add_assignment(self, assignment):
        new_clauses = set()
        for clause in self._clauses_set:
            new_literals = set()
            for literal in clause.literals:
                if literal.variable not in assignment:
                    new_literals.add(literal)
                elif assignment[literal.variable] != literal.add_negation:
                    new_literals = set()
                    break
            if len(new_literals) != 0:
                new_clauses.add(Clause(*new_literals))
        self._clauses_set = new_clauses
        self._clauses = list(self._clauses_set)


    def __eq__(self, other):
        return self._clauses == other._clauses and \
            self._clauses_set == other._clauses_set

    def __str__(self):
        return '/\\'.join(map(str, self.clauses))
