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
