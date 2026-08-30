from utils.utils import add_implication_to_list

"""
A cycle/sequence enumeration routine that enumerates
aperiodic increasing powers of two cycles 
"""
def gen_powers_of_two_cycle_model(full_iters : int):
    horizontal_implications = {1:{3}, 
                               2:{4}, 
                               3:{5,7}, 
                               4:{6,8}
                               }
    vertical_implications = {0:{0}, 
                             1:{0}, 
                             2:{0}, 
                             3:{2}, 
                             4:{1}, 
                             5:{4}, 
                             6:{3}, 
                             7:{4}, 
                             8:{3}
                             }
    diagonal_sequences = [
        [1,2],
        [3,4],
        [5,6,7,8]
    ]
    current_sequence = [5,6,7,8]

    # first mapping
    m1 = {5:9, 6:10, 7:11, 8:12}
    # second two mappings
    m2 = {9:5, 10:5, 11:5, 12:6}
    m3 = {9:7, 10:7, 11:7, 12:8}

    # current sequence length
    clen = 4

    for _ in range(full_iters):
        print(f"Current Sequence : {current_sequence}")
        next_sequence = []
        for i in range(clen):
            next_sequence.append(m1[current_sequence[i]])

        # read off implications
        for i in range(clen):
            add_implication_to_list(horizontal_implications, current_sequence[i], next_sequence[i])
            if i == clen-1:
                add_implication_to_list(vertical_implications, next_sequence[i], current_sequence[0])
            else:
                add_implication_to_list(vertical_implications, next_sequence[i], current_sequence[i+1])

        # store the next value in the diagonal sequence list
        diagonal_sequences.append(next_sequence)
        current_sequence = next_sequence
        next_sequence = []

        next_sequence_1 = []
        next_sequence_2 = []
        current_sequence_extended = current_sequence + current_sequence
        for i in range(clen):
            next_sequence_1.append(m2[current_sequence[i]])
            next_sequence_2.append(m3[current_sequence[i]])
            current_sequence_extended.append(current_sequence[i])

        # order doesn't matter
        next_sequence = next_sequence_1 + next_sequence_2

        # double sequence length count
        clen *= 2

        # read off implications
        for i in range(clen):
            add_implication_to_list(horizontal_implications, current_sequence_extended[i], next_sequence[i])
            if i == clen-1:
                add_implication_to_list(vertical_implications, next_sequence[i], current_sequence[0])
            else:
                add_implication_to_list(vertical_implications, next_sequence[i], current_sequence_extended[i+1])

        # store the next value in the diagonal sequence list
        diagonal_sequences.append(next_sequence)
        current_sequence = next_sequence
        next_sequence = []

        print(f"New Sequence : {current_sequence}")
        print("Updated Implication List : ")
        print(f" Horizontal : {horizontal_implications} ")
        print(f" Vertical : {vertical_implications} ")
        print("-----------------------------")

        return (horizontal_implications, vertical_implications)