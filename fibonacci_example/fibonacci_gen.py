from utils.utils import add_implication_to_list

"""
A cycle/sequence enumeration routine that enumerates
aperiodic fibonacci length blocks inside power of two cycle expansions
"""
def gen_fibonacci_encoding_model(full_iters : int):
    """
    Fibonacci encoding using Wang Tiles and AEA formula format
    """
    horizontal_implications = {1:{5}, 
                               2:{6}, 
                               3:{7}, 
                               4:{8},
                               5:{"A"},
                               6:{"D"},
                               7:{"E"},
                               8:{"F"}
                               }
    vertical_implications = {0:{0}, 
                             1:{0}, 
                             2:{0}, 
                             3:{0}, 
                             4:{0}, 
                             5:{2}, 
                             6:{3}, 
                             7:{4}, 
                             8:{1}
                             }
    diagonal_sequences = [
        [1,2,3,4],
        [5,6,7,8],
        ["A","D","E","F"]
    ]
    current_sequence = ["A","D","E","F"]

    # relevant mapping tables
    m1 = {}
    m2 = {}

    # current sequence length
    clen = 4

    for _ in range(full_iters):
        #print(f"Current Sequence : {current_sequence}")
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

        #print(f"New Sequence : {current_sequence}")
        #print("Updated Implication List : ")
        #print(f" Horizontal : {horizontal_implications} ")
        #print(f" Vertical : {vertical_implications} ")
        #print("-----------------------------")

    return (horizontal_implications, vertical_implications)