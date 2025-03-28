def is_pangram(sentence):
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in sentence.lower():
            return False
    return True