def convert(number):
    result = str(number)
    raindrops = ""
    if number % 3 == 0:
        raindrops += "Pling"
    if number % 5 == 0:
        raindrops += "Plang"
    if number % 7 == 0:
        raindrops += "Plong"
    
    return result if len(raindrops) == 0 else raindrops