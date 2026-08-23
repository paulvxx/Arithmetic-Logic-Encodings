# First Order Logic Encodings

## Overview

This repository is a collection of programs and explainations behind those programs with focus around model theory, finite and cellular automaton, Turing Machines, First order Logic, Entscheidungsproblem, and computational theory.

The Entscheidungsproblem ("decision problem" in German) was a mathematical question posed by the mathematicians David Hilbert and Wilhelm Ackermann in 1928. It asked for a general solution or finite procedure to determine if a logical formula is universally valid (meaning it holds under all possible interpretations), or equivalently on the other end, satisfiable (meaning it holds true under at least one interpretation). The hope was that if such a procedure existed, all problems posed by mathematics with logical formulas could be solved algorithmically. Gödel’s first incompleteness theorem was published in 1931, which states that in a formal system bound by logical axioms or rules that can, in short, encode basic arithemtic, contains formable statements within the system that cannot be proven true (or false) inside the system. This paved the way towards showing the Entscheidungsproblem does not have a general solution. In 1936, mathematicians Alan Turing and Alonzo Church showed that such a general procedure does not exist, meaning no single algorithm could exist that finishes in a finite amount of time, and yields the correct answer 100% of the time. However, this does not mean many algorithms can exist for solving restricted subproblems of the Entscheidungsproblem. For example, when the Entscheidungsproblem is restricted to two bounded quantifier variables, the problem is fully decidable by procedures. 

See (https://plato.stanford.edu/entries/church-turing/decision-problem.html)

## Computational Methods

The prefix class AEA (for all x, exists y, for all z P(x,y,z) is true) is one of the smallest sub-classes of Entscheidungsproblem statements which is undecidable --- meaning even for statements of those types --- where P does not contain extra or more bounded variables --- there is no decision procedure to determine if such a sentence is valid. In 1962, (reference needed) it was shown that the AEA class restricted to only binary relations was unsolvable. 

Consequently, any formula of the form AEA+  (+ = one or more repetitions,  i.e. AEA, AEAA, AEAAA, etc.) is unsolvable. Logical formulas of the type AEA+ provide natrual sturctural equisatisfiability relationships between uninterpreted domains and domains over the natural numbers (Büchi’s Reduction Lemma). For instance, one can take a sentence (for all x, exists y, for all z P(x,y,z) is true) and generate an equisatisfiable one of the form (for all x, for all z in N : P(x,x+1,z) is true). This uses a trick called Skolemnization, which interprets the existentially bound quantifier (i.e. y in the previous specific formula class). and turns it into a function of any preceding universal quantifiers (i.e. x), so one replaces exists y with y = f(x), or just f(x). The first universal quantifier (for all x) requires every "element" has its own existential "witness" by "applying" f. Hence the pattern  x, f(x), f(f(x)), f(f(f(x))), etc. represents the structure of generating elements of AEA+, and is equivalent by structure to the Von-Neumann or Peano formulation of the natural numbers.

This makes formulations of type AEA+ desirable for expressing computations since they can be visualized on a grid of certain dimension (for binary prediates, 2 dimensions, for ternary ones, three dimensions, etc). 
Binary predicates boil the satisfiability or validity problem to computatonal behavior on the first quadrant of the coordinate plane where computation can be encoded by filling out squares with "colors" or "markings" (predicate choices). The 1962 reference to undecidability naturall follows this same idea, but formalizes these concepts using "Wang Tiles" which mark tiles with colors on a 2d grid, with the only constraints being adjacency matching criteria by matching squares with common edges next to eachother. While general Turing-Completness is achieveable this way, it is notoriously nontrivial to encode certain non-periodic patterns this way. Certain extra quantifiers (i.e. AEAA) might be useful to help point to previous positions or references without have to encode that information within strict adjacency relations.

## Explicit Sequences or patterns

Most computational examples in this repository rely on basic or simple arithemtic patterns --- such as encoding the triangular numbers, powers of two, or Fibonacci Numbers. Different folders are decidcated to different kinds of computational problems.

## Challenges

First-order Logic natively has no concept of "order" or "memory". In first order logic, there are domains, predicates, and truth assignments and formulae (and if permissible, equality). While computation can be expressed within these constraints itself (by linking its behavior to satisfiability), it relies on immense scaffolding and strict rules or propositions --- easily spanning dozens if not hundreds of clasues or formula components.  

Furthermore, in some examples, it is demonstrated that computation can be encoded without a unique origin anchor. The point origin (0,0) can be specifcied by adding an existential to the front of an AEA type statement (actually, from a techincal standpoint, a universal statement is trivially true under the idea that the empty domain interpretation satisfies it --- requiring a leading  existential forces a non-empty domain, but only so to reference the origin and zero exactly once to assert a starting point).  

Most examples, however, tend to rely on a uniquely global origin anchor. That is, all the exhaustive combination of propositional occurrences happening at the point (0,0) are unique and do not occur anywhere else on the 2-d plane (for example, the underlying phenomenon is if P(0,0) is true, P(a,b) is never true if at least one of a or b is non-zero, i.e. a + b > 0).

The other examples that don't rely on a globally unique origin anchor replace that concept with cyclic patterns along the main diagonal of the first quadrant and diagonal lines moving away from the diagonal center in one direction (i.e. Y=X, Y=X+1, Y=X+2, Y=X+3, etc.).
