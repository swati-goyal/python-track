def is_paired(input_string):
    stack = []
    open_brackets = "[{("
    closed_brackets = "]})"

    for char in input_string:
        if char in open_brackets:
            stack.append(char)
        elif char in closed_brackets:
            if not stack or open_brackets[closed_brackets.index(char)] != stack.pop():
                return False

    return not stack
