# Arithmetic-Logic-Encodings
The goal of this project is to create a program that can convert any imperative/recursive program into a first order model.

More specifically (To be completed), this project serves as an implementation for parsing basic arithmetic imperative code, recursive code, and translating it into an equivalent first-order sentence without equality, only using binary predicates, and of the prenex normal form AEAA. Proving invariants about the original program can be converted into an AEAA sentence, such that the invariant or correctness of the program is true if and only if the resulting sentence does not have a contradiction. 

For example, one might wish to convert the program:

x = n (any number)
s = 0
for i = 0; i < x; i = i+1 : s = s + 1;


and prove that, say, x = (n^2 - n)/2. With the solver tool to be implemented, one can effectively write the code in a specific syntax, have it parsed, and generate a first order sentence that proves the correctness of the program and the property of it.

Read the journals for more information about the math behind how to translate any recursive/imperative program and a desired/specific property of it, into an equisatisfiable first order sentence.

For instance, in the paper, it is shown that if the sentence is satisfiable 

for all x, z, z' in N = {0,1,2,3,...}:
A(0,0) && 
B(0,0) &&
C(0,0) && 
(A(z,x) && A(z',x)) -> (z = z')) && 
(B(z,x) && B(z',x)) -> (z = z')) && 
(C(z,x) && C(z',x)) -> (z = z')) && 
(B(0,x) -> A(0, x+1)) && 
(B(x+1, z) -> B(x, z+1)) && 
(C(x,z) && A(x,z)) -> ~A(x+1, z+1)) && 
(~C(x,z) && A(x,z)) -> A(x+1, z+1)) && 
(C(x,z) -> (C(x, z+1) || C(x+1, z+1))) && 
(B(0,x) && C(z,x)) -> ~C(z, x+1)) && 
(~B(0,x) && C(z,x)) -> C(z, x+1)) && 
(A(0,x) && C(z,x)) -> B(z,x))

then one can show that for natural numbers a,b,c,n : (A(a,n) && B(b,n)) iff n = binomial(a+b+1,2) + a.  And if (A(a,n) && B(b,n)), then C(c,n) is true if and only if (a + b = c).  


