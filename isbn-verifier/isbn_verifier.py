def is_valid(isbn):
    
    isbn = list(str(isbn.replace('-','')))

    if len(isbn) < 10 or len(isbn) > 10:
        return False

    if 'X' in isbn:
        index = isbn.index('X')
        if index != 9:
            return False
        isbn[index] = '10'

    multiplier = 10
    sum_of_numbers = 0
    for num in isbn:
        if num.isalpha():
            return False
        sum_of_numbers += int(num) * multiplier
        multiplier -=1
    
    return sum_of_numbers % 11 == 0