def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    for digit in digits:
        if digit >= input_base or digit < 0:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    
    if input_base == 10:
        return find_mod(digits, output_base)
    elif output_base == 10:
        return convert_to_base_ten(digits, input_base)
    else:
        digits_in_base_ten = convert_to_base_ten(digits, input_base)
        return find_mod(digits_in_base_ten, output_base)


def find_mod(digits, output_base):
    number = int("".join([str(i) for i in digits]))
    result = []

    while number >= output_base:
        remainder = number % output_base
        result.append(remainder)
        number //= output_base

    result.append(number)
    return list(reversed(result))

def convert_to_base_ten(digits, input_base):
    power_list = [input_base ** i for i in range(0, len(digits))]
    my_list = list(zip(digits, reversed(power_list)))
    result = [digit * multiplier for digit, multiplier in my_list]
    return [int(i) for i in str(sum(result))]