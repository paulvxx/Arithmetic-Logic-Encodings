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

def implication_list_to_cnf(h_implication_list, v_implication_list, conversion="mutually_disjoint"):
    """
    Converts a list of adjacency implications (key-value dictionary) to 
    a representation format of conjunctions of disjunctions
    (conjunctive normal form) ∀x∃y∀z P(x,y,z) where P is quantifier-free
    """
    predicates = set(h_implication_list.keys()).union(set(v_implication_list.keys()))
    clauses = []

    # horizontal implications
    for h in h_implication_list.keys():
        clause = [(h,'z','x',False)]
        for adj in h_implication_list[h]:
            clause.append((adj,'z','y',True))
        clauses.append(clause)

    # vertical implications
    for v in v_implication_list.keys():
        clause = [(v,'x','z',False)]
        for adj in v_implication_list[v]:
            clause.append((adj,'y','z',True))
        clauses.append(clause)

    # mutually exclusive predicates conditions
    for p in predicates:
        for q in predicates:
            if p != q:
                clause = [(p,'x','z',False), (q,'x','z',False)]
                clauses.append(clause)

    # return the CNF format of predicate logical formulas
    return clauses
