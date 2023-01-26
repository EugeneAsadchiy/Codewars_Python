def unique_in_order(sequence):
    sequence = list(sequence)
    b = []

    # print(sequence)
    if len(sequence) < 2:
        b = sequence
        return b

    if sequence.count(sequence[0]) == len(sequence):

        b.append(sequence[0])
        return b
    if sequence[0] == sequence[1]:
        # b.append(sequence[0])
        sequence.pop(1)
    # print(b, sequence)
    # b.append(sequence[0])

    if len(sequence) >= 2:
        for i in range(len(sequence) - 1):
            # if sequence[0] == sequence[1]:
            #     b.append(sequence)
            if sequence[i] == sequence[i + 1]:
                continue
            else:
                b.append(sequence[i])
        if len(sequence) == 2:
            b.append(sequence[-1])
            return b
        if len(sequence) != 2:
            if sequence[-1] != b[-1]:
                b.append(sequence[-1])
    else:
        b = sequence

    return b