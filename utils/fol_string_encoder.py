"""
Utilities for encoding functions from structural format to string-formulas
"""

def format_literal(literal_tuple):
    """
    Converts a single 4-tuple (predicate_id, arg1, arg2, sign) into a string literal.
    
    If predicate_id is an integer or a numeric string, it is converted to 'P_X'.
    If sign is False, a negation symbol (~) is prepended.
    """
    pred, arg1, arg2, sign = literal_tuple
    
    # Format the predicate symbol (e.g., 3 -> P_3)
    if isinstance(pred, int):
        pred_str = f"P_{pred}"
    else:
        return
      
    # Prepend negation symbol '~' if sign is False
    negation = "~" if not sign else ""
    return f"{negation}{pred_str}({arg1},{arg2})"
