def is_armstrong_number(number):
    digits = list(str(number))
    power = len(digits)
    new_list = []
    for digit in digits:
        num = int(digit)
        new_list.append(num ** power)
    return sum(new_list) == number