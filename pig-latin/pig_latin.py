VOWELS = [i for i in "aeiou"]
CONSONANTS = [i for i in "bcdfghjklmnpqrstvwxyz"]


def translate(text):
    text = text.split()
    result = []
    for word in text:
        word = pigify(word)
        result.append(word)
    return result[0] if len(result) == 1 else " ".join(result)


def add_ay(s):
    return s + "ay"


def special_pigies(word, pig):
    return add_ay(word.split(pig)[1] + pig)


def pigify(word):
    if word.startswith(("xr", "yt", *VOWELS)):
        return add_ay(word)
    if word.startswith(("", *CONSONANTS)):
        if word.startswith("qu"):
            return special_pigies(word, "qu")
        if word.startswith("squ"):
            return special_pigies(word, "squ")
        if word.startswith("y"):
            return special_pigies(word, "y")
        for index, letter in enumerate(word):
            if letter in ("y", *VOWELS):
                return add_ay("".join([word[index:] + word[:index]]))
