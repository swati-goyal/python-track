def response(hey_bob):
    hey_bob = str(hey_bob)
    hey_bob = hey_bob.strip()
    hey_bob = hey_bob.strip("\t")
    hey_bob = hey_bob.strip("\n")
    hey_bob = hey_bob.strip("\r")

    if hey_bob.isupper():
        if hey_bob[-1] == '?':
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif len(hey_bob) == 0:
        return "Fine. Be that way!" 
    elif hey_bob[-1] == '?':
        return "Sure." 
    else:
        return "Whatever."