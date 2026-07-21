# Arithmetic-Logic-Encodings
The goal of this project is to create a program that can convert any imperative/recursive program into a first order model.

More specifically (To be completed), this project serves as an implementation for parsing basic arithmetic imperative code, recursive code, and translating it into an equivalent first-order sentence without equality, only using binary predicates, and of the prenex normal form AEAA. Proving invariants about the original program can be converted into an AEAA sentence, such that the invariant or correctness of the program is true if and only if the resulting sentence does not have a contradiction. 

For example, one might wish to convert the program:

x = n (any number)
s = 0
for i = 0; i < x; i = i+1 : s = s + 1;


and prove that, say, x = (n^2 - n)/2. With the solver tool to be implemented, one can effectively write the code in a specific syntax, have it parsed, and generate a first order sentence that proves the correctness of the program and the property of it.
