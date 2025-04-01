def flatten(iterable):
    flat_array = []
    for item in iterable:
        if item is None:
            continue
        if isinstance(item, int):
            flat_array.append(item)
        else:
            flat_array.extend(flatten(item))
    return flat_array
