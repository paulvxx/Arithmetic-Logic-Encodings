"""
Main python program to run scripts
"""

from powers_of_two_example import powers_of_two_gen
from utils import utils

h_iList, v_iList = powers_of_two_gen.print_powers_of_two_cycle(4)

cnf_format = utils.implication_list_to_cnf(h_iList, v_iList)

for c in cnf_format:
    print(c)