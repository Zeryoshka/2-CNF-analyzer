import boolean

# SATISFIABILITY TESTS
def test_sat1():
    cnf = "p /\\ (p -> q) /\\ (p -> ~r) /\\ (r \\/ ~s) /\\ (s \\/ ~q)"
    result = boolean.is_satisfiable(cnf)
    assert (not result)

def test_sat2():
    cnf = "p /\\ (p -> q) /\\ (q -> r) /\\ ~r"
    result = boolean.is_satisfiable(cnf)
    assert (not result)

def test_sat3():
    cnf = "(~p \\/ q) /\\ (~p \\/ r) /\\ (~q \\/ r) /\\ (p \\/ ~q) /\\ (~p \\/ ~q) /\\ (~p \\/ ~r)";
    result = boolean.is_satisfiable(cnf)
    assert(result)

def test_sat4():
    cnf = "(p -> q) /\\ (q -> ~r) /\\ (r -> p)"
    result = boolean.is_satisfiable(cnf)
    assert(result)

def test_sat5():
    cnf = "(p \\/ t) /\\ (p -> q) /\\ (q -> r) /\\ (~r \\/ s) /\\ (~t \\/ z) /\\ ~z /\\ ~s"
    result = boolean.is_satisfiable(cnf)
    assert(not result)

# SATISFYING ASSIGNMENT TESTS
def test_assign1():
    cnf = "(p \\/ q) /\\ (q \\/ r) /\\ (r \\/ s) /\\ (s \\/ t) /\\ (t \\/ q)"
    a = boolean.sat_assignment(cnf)
    p = a['p']
    q = a['q']
    r = a['r']
    s = a['s']
    t = a['t']
    assert ((p or q) and (q or r) and (r or s) and (s or t) and (t or q))

def test_assign2():
    cnf = "(p -> q) /\\ (q -> r) /\\ (q -> t) /\\ (q -> s) /\\ (t -> s) /\\ (s -> ~p)"
    a = boolean.sat_assignment(cnf)
    p = a['p']
    q = a['q']
    r = a['r']
    s = a['s']
    t = a['t']
    assert (((not p) or q) and ((not q) or r) and ((not q) or t) and ((not q) or s) and ((not t) or s) and ((not s) or (not p)))

def test_assign3():
    cnf = "(~p \\/ q) /\\ (~p \\/ r) /\\ (~q \\/ r) /\\ (p \\/ ~q) /\\ (~p \\/ ~q) /\\ (~p \\/ ~r)"
    a = boolean.sat_assignment(cnf)
    p = a['p']
    q = a['q']
    r = a['r']
    assert (((not p) or q) and ((not p) or r) and ((not q) or r) and (p or (not q)) and ((not p) or (not q)) and ((not p) or (not r)))

def test_assign4():
    cnf = "(p -> q) /\\ (q -> ~r) /\\ (r -> p)"
    a = boolean.sat_assignment(cnf)
    p = a['p']
    q = a['q']
    r = a['r']
    assert (((not p) or q) and ((not q) or (not r)) and ((not r) or p))

def test_assign5():
    cnf = "(p \\/ q) /\\ (p \\/ ~q) /\\ (q -> r) /\\ (~q -> s) /\\ (r -> s)"
    a = boolean.sat_assignment(cnf)
    p = a['p']
    q = a['q']
    r = a['r']
    s = a['s']
    assert ((p or q) and (p or (not q)) and ((not q) or r) and (q or s) and ((not r) or s))
