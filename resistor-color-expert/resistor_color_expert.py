COLORS = "black brown red orange yellow green blue violet grey white".split()
TOLERANCES = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}
UNITS = ["ohms", "kiloohms", "megaohms"]


def resistor_label(colors):
    if len(colors) > 3:
        *bands, multiplier, tolerance = colors
    else:
        bands, multiplier, tolerance = colors, COLORS[0], None

    resistance = 0.0

    for band in bands:
        resistance = resistance * 10 + COLORS.index(band)
    resistance *= 10 ** COLORS.index(multiplier)

    power = 0
    while resistance >= 1000:
        resistance /= 1000
        power += 1
    
    # Read about :n in python strings
    total_value = f"{resistance:n} {UNITS[power]}"
    if tolerance:
        total_value += f" ±{TOLERANCES[tolerance]}%"
    return total_value
