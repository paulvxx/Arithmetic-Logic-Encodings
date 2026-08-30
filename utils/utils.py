"""
Shorthand utility to add implication to list
"""
def add_implication_to_list(ilist : list, key, value):
    if key not in ilist:
        ilist[key] = {value}
    else:
        ilist[key].append(value)
