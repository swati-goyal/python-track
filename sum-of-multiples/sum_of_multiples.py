def sum_of_multiples(limit, multiples):
    list_of_numbers = []
    for item in multiples:
        if item == 0:
            continue
        number_of_multiples = limit // item
        list_of_numbers += [
            i * item for i in range(1, number_of_multiples + 1) if i * item < limit
        ]
    return sum(list(set(list_of_numbers)))
