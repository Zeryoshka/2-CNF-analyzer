# boolean-template
Template Repository for HW 1

## Task for HW 1

The input is a Boolean formula in 2-CNF, given as a string of symbols. A *literal* is a variable name 
(at least any small Latin letter should be a legal variable name) or its negation, denoted by `~`.
A *clause* is either a literal, or `(L1 \/ L2)`, or `(L1 -> L2)`, where `L1` and `L2` are literals.
Finally, the *2-CNF* is either one clause or a conjunction of two or more clauses, where conjunction is
denoted by `/\`.

Example: `p /\ (p -> q) /\ (p -> ~r) /\ (~r \/ ~s) /\ (s \/ ~q)`

The *first* task is to check whether the given 2-CNF is satisfiable. The *second* task is, given a 2-CNF,
report that it is not satisfiable or return one of its satisfying assignments. Solving only the first task
gives you a half grade (2 points out of 4). Solving both gives 4 points.

### Technical Details

In order for the automated test to work fine, please carefully adhere the following technical instructions.
Your solution should be implemented in Python3, in a file named `boolean.py`. For the first task, you should
implement a function called `is_satisfiable`, which takes the string with the 2-CNF as an argument and
returns either `True` (satisfiable) or `False` (not satisfiable). The second task should be implemented as
a function called `sat_assignment`. This function also takes one argument (string) and returns an associative
array (dictionary) with the satifying assignment (e.g., `{ 'p': True, 'q': False, 'r': True }`) or `None`,
if the 2-CNF is not satisfiable.

**Warning:** the automatic tests run several iterations of your functions, with different CNFs.
If you use global variables, please make sure that their values from previous iterations do not 
make the next one work incorrectly.

### Practical Info

The preferable way to submit the assignment is via GitHub classroom, [invite link](https://classroom.github.com/a/ZRHmjSA-),
see also [course webpage](https://homepage.mi-ras.ru/~sk/lehre/dm_hse/) for details.
After submitting, you shall see the results of automated testing, which will be used for grading.
As a fallback, it is also possible to submit via email to <sk@mi-ras.ru>. The same address may be used for 
asking questions. 

The deadline is **October 5, 2021** anywhere-on-Earth, and it is **strict**. If you know you will not be able
to finish the task before the deadline, please inform **in advance**.

**Cheating will not be tolerated.** 
The notion of cheating here includes, besides usage of other students' code, also the following: (1) altering
the test file `boolean_test.py` (removing tests which fail etc); (2) hardcoding the correct results for given
tests. Any detected case of cheating will result in unchangable mark of 0 points for HW 1.