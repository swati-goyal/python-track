class SpaceAge:
    EARTH_YEAR = 365.25 * 3600 * 24

    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        year = 1 / 0.2408467
        return round((self.seconds / self.EARTH_YEAR) * year, 2)

    def on_venus(self):
        year = 1 / 0.61519726
        return round((self.seconds / self.EARTH_YEAR) * year, 2)

    def on_earth(self):
        year = 1 / 1.0
        return round((self.seconds / self.EARTH_YEAR) * year, 2)

    def on_mars(self):
        year = 1 / 1.8808158
        return round((self.seconds / self.EARTH_YEAR) * year, 2)

    def on_jupiter(self):
        year = 1 / 11.862615
        return round((self.seconds / self.EARTH_YEAR) * year, 2)

    def on_saturn(self):
        year = 1 / 29.447498
        return round((self.seconds / self.EARTH_YEAR) * year, 2)

    def on_uranus(self):
        year = 1 / 84.016846
        return round((self.seconds / self.EARTH_YEAR) * year, 2)

    def on_neptune(self):
        year = 1 / 164.79132
        return round((self.seconds / self.EARTH_YEAR) * year, 2)
