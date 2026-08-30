"""
Utilities for encoding functions from structural format to string-formulas
"""

def format_literal(literal_tuple):
    """
    Converts a single 4-tuple format (predicate_id, arg1, arg2, sign) into a string literal.

    If predicate_id is an integer or a numeric string, it is converted to 'P_X'.
    If sign is False, a negation symbol (~) is prepended.
    """
    pred, arg1, arg2, sign = literal_tuple
    
    # Format the predicate symbol (e.g., 3 -> P_3)
    if isinstance(pred, int):
        pred_str = f"P_{pred}"
    elif isinstance(pred, str):
        pred_str = f"{pred.capitalize()}"
    else:
        raise TypeError("Error : Predicate symbol must either be a String or Integer.")
    
    # Prepend negation symbol '~' if sign is False
    negation = "~" if not sign else ""
    return f"{negation}{pred_str}({arg1},{arg2})"


def to_fol_cnf_formula(clauses, wrap_single=False, pretty=False):
    """
    Converts a list of list of 4-tuples into a First-Order Logic formula in the AEA prefix class.
    
    Parameters:
    -----------
    clauses : list of list of tuple
        The input clauses, where each clause is a list of 4-tuples.
    wrap_single : bool, default False
        Whether to wrap single-literal clauses in parentheses, e.g., (P_5(z,x)) instead of P_5(z,x).
    pretty : bool, default False
        Whether to pretty-print the formula with indentation and newlines.
    
    Returns:
    --------
    str
        The formatted FOL string.
    """
    if not clauses:
        return "∀x∃y∀z { True }"
        
    clause_strings = []
    for clause in clauses:
        literals = [format_literal(lit) for lit in clause]
        clause_str = " || ".join(literals)
        
        # Wrap in parentheses if there are multiple literals, or if wrap_single is True
        if len(literals) > 1 or wrap_single:
            clause_str = f"({clause_str})"
            
        clause_strings.append(clause_str)
        
    if pretty:
        # Multi-line pretty-printed output
        indent = "  "
        joined_clauses = f"\n{indent}&& ".join(clause_strings)
        return f"∀x∃y∀z {{\n{indent}{joined_clauses}\n}}"
    else:
        # Single-line output
        joined_clauses = " && ".join(clause_strings)
        return f"∀x∃y∀z {{ {joined_clauses} }}"
