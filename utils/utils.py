import math

"""
Shorthand utility to add implication to list
"""
def add_implication_to_list(ilist : list, key, value):
    """
    Shorthand for adding new element to value set for key-value dictionary pair
    """
    if key not in ilist:
        ilist[key] = {value}
    else:
        ilist[key].add(value)

def read_implications_from_diagonals(horizontal_implications : dict, vertical_implications : dict, 
            current_line : list, next_line : list):
    """
    Helper routine to extract implications from two lists representing cycles along diagonal lines
    """
    c_len = len(current_line)
    n_len = len(next_line)
    # if either list is empty, raise an exception
    if (c_len * n_len) == 0:
        raise ValueError("Error : Cycle lists must be non-empty")

    c_expanded = current_line
    n_expanded = next_line
    cycle_length = c_len
    # if the lengths are not equal, expand the cycles continuously (least common multiple) until the periods match
    if c_len != n_len:
        cycle_length = math.lcm(c_len, n_len)
        # calculate number of times each cycle has to be extended
        c_repetitions = cycle_length // c_len
        n_repetitions = cycle_length // n_len
        c_expanded = []
        n_expanded = []
        # expand the first cycle
        for _ in range(c_repetitions):
            c_expanded.extend(current_line)
        # expand the second cycle:
        for _ in range(n_repetitions):
            n_expanded.extend(next_line)

    # read off implications
    for i in range(cycle_length):
        add_implication_to_list(horizontal_implications, c_expanded[i], n_expanded[i])
        if i == cycle_length-1:
            add_implication_to_list(vertical_implications, n_expanded[i], c_expanded[0])
        else:
            add_implication_to_list(vertical_implications, n_expanded[i], c_expanded[i+1])
    

def implication_list_to_cnf_AEA(h_implication_list, v_implication_list, explicit_disjoint=True):
    """
    Converts a list of adjacency implications (key-value dictionary) to 
    a representation format of conjunctions of disjunctions
    (conjunctive normal form) ∀x∃y∀z P(x,y,z) where P is quantifier-free
    """
    clauses = []

    # horizontal implication clauses
    for h in h_implication_list.keys():
        # demorgan's laws applied to the antecedent
        clause = [(h,'z','x',False)]
        for adj in h_implication_list[h]:
            clause.append((adj,'z','y',True))
        clauses.append(clause)

    # vertical implication clauses
    for v in v_implication_list.keys():
        # demorgan's laws applied to the antecedent
        clause = [(v,'x','z',False)]
        for adj in v_implication_list[v]:
            clause.append((adj,'y','z',True))
        clauses.append(clause)

    # mutually exclusive predicates conditions
    if not explicit_disjoint:
        # avoid listing out the mutually disjoint conditions 
        return clauses
    
    predicates = set(h_implication_list.keys()).union(set(v_implication_list.keys()))
    # iterate through all unordered distinct pairs (a,b) of all predicates (a != b)
    while len(predicates) != 0:
        # select any predicate from the set it if is not empty
        p = next(iter(predicates))
        remaining = predicates.copy()
        # remove it from the set of remaining predicates
        remaining.difference_update({p})
        for r in remaining:
            clause = [(p,'x','z',False), (r,'x','z',False)]
            clauses.append(clause)
        # iterate through the next loop
        predicates = remaining
            
    # return the CNF format of predicate logical formulas
    return clauses
