# Powers of Two 

## Overview

This sub-repository (or folder) provides two working examples of encoding expoentnial (doubling) behavior within a cellular automata or two dimensional grid using only local adjacency rules.

## Origin-less computation

The main challenges of encoding a power-of-two grid cleanly without any structural placements (such as a point of true origin reference) come with the fact that unlike some other examples (i.e. the examples involving triangular numbers), computation cannot simply "unfold" from a single point and expand outward, it must be represented dynamically by expanding equivalence classes or cycles. Results established by authors Emmanuel Jeandel and Michaël Rao indicated that the minimum number of Wang tiles to form aperiodic relationships is 11 (in equivalent translations, distinct truth-value combinations across all predicates or states). In other words, 10 or less states will either raise unsatisfiable problems, or models with periodic relationships. The solution for encoding or representing powers of two along a grid involve 13 different states or tiles. It is similar in Nature to Robinson's tiling set initially containing 56 tiles, but instead of using dynamically expanding squares or corners, it uses cycle patterns along diagonal lines like Y=X, Y=X+1, Y=X+2, Y=X+3, etc.

[Reference to robinson tiles or the 11-minimum tiling set?]

## Solution

The main solution is to encode aperiodic behavior using diagonal lines on one octant (dividing the quadrant diagonally) of a 2-d grid, while leaving the other half blank. The solution involves using 13 states or symbols {0,1,2,3,4,5,6,7,8,9,10,11,12} which must inhibit specific properties. We first express the solution with equality relationships using a functional symbol P(a,b) which maps to one of 13 elements, and where one side of the equality must be a number less than 13, still holding under a quantifier structure AEA (or rather, by using Büchi’s Reduction Lemma first, AA under the interpretation of natural numbers) which is in Conjunctive Normal Form (CNF). 

At that point, relationships like P(a,b) = c can be converted to raw predicates by treating each number 0 through 12 as a truth value combination (i.e. for example, represening P(a,b) = 5 by not A(a,b) and B(a,b) and not C(a,b) and D(a,b)) or by a designated predicate that is mutually exclusive with other predicates, and applying De-Morgan's Laws (for the first conversion  more so) can restore the formula back into CNF.

### Dynamically Expanding Cycles

Since the origin cannot be unique, we cannot rely on a starting case that outwardly expands itself at point (0,0) on the plane N^2. 
Instead, we can translate the starting pivot to an infinitely periodic alternating cycle along the main diagonal. 

The first symbol '0' can be marked along the strict lower half of the main diagonal (i.e. X,Y where X < Y). For convention, we will represent terms d_i as sequence memebers whose values are cycle patterns along the line (Y = X + i).

The initial case along the main diagonal itself can serve as the initial case, and we use a 2-cycle (1,2) to initiate this.

d_0 = (1,2)

Cycles should be interpreted from left-to-right, as the "relative" beginning on the left, and "relative" end on the right. So along the diagonal, for d_0, would imply P(0,0)=1, P(1,1)=2, P(2,2)=1, P(3,3)=2, etc. etc.

The next case is also a semi-starting case, which consists of another 2-cycle

d_1 = (3,4)

Like d_0, this can be interpreted along the diagonal Y = X + 1 as P(0,1)=3, P(1,2)=4, P(2,3)=3, P(3,4)=4, ...

At this point, it is worth discussing how to actually formulate these cyclic patterns into logical implications or statements. 

You might have the grid visualized like this:

1 3 ...
0 2 4 ...
0 0 1 3 ...
0 0 0 2 4 ...
0 0 0 0 1 3 ...
0 0 0 0 0 2 4 ...

etc.

The rule to determine which implications or statements should be imposed is to align the cycles together side-by-side in order (d_i, d_i+1) (and if necessary, repeat/expand them until they have the same periodic length). For example, to align (1,3) and (2,4) such that they are written across rows (2 columns --- one for each cycle) would be:

(1 2)
(3 4)

Then two cycle characters (i.e. 1 and 3 for example) aligned directly next to eachother are horizontally adjacent. 

A cycle character on the right (second cycle) along with the cycle character on the row immediately following it (or wrap-around if necessary), are vertically adjacent (i.e. 2 and 3 for example). 

Iterating across cycle sequence members in this manner from the relative beginning to relative end of both cycles will yield all locally present horizontal or vertical adjacency rules that must be captured.



## Programs 

