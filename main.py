"""
Main python program to run scripts
"""

from powers_of_two_example import powers_of_two_gen
from utils import utils, fol_string_encoder

h_iList, v_iList = powers_of_two_gen.print_powers_of_two_cycle(4)

cnf_format = utils.implication_list_to_cnf_AEA(h_iList, v_iList)

formula_str = fol_string_encoder.to_fol_cnf_formula(cnf_format, pretty=True)

print(formula_str)