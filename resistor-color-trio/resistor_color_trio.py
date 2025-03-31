mapping = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def label(colors):

    if len(colors) < 3:
        raise ValueError("correct number of resistance colors should be provided")

    color_values = [mapping[color] for color in colors]
    resistance = 10 * color_values[0] + color_values[1]

    total_resistance = resistance * (10 ** color_values[2])

    zeroes = sum(1 for i in str(total_resistance) if i == "0")

    if 0 <= zeroes < 3:
        return str(total_resistance) + " ohms"
    elif 3 <= zeroes < 6:
        return str(total_resistance // (10**3)) + " kiloohms"
    elif 6 <= zeroes < 9:
        return str(total_resistance // (10**6)) + " megaohms"
    else:
        return str(total_resistance // (10**9)) + " gigaohms"
