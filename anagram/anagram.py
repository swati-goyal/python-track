def find_anagrams(word, candidates):
    return [
        w
        for w in candidates
        if sorted(w.casefold()) == sorted(word.casefold()) and w.casefold() != word.casefold()
    ]
