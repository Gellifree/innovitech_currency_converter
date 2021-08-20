import file_handler

class Converter():
    def __init__(self):
        self.fh = file_handler.FileHandler()

    def convert_from_eur(self, value, target):
        return value * self.fh.read_exchange()['rates'][target]

    def convert_to_eur(self, value, base):
        return value / self.fh.read_exchange()['rates'][base]

    def convert(self, base, target, value):
        # Konvertáljuk át az értéket, a kiinduló alapból (base) Euróba
        # Az euróban megkapott értéket konvertáljuk át a cél típusba (target)
        # Majd adjuk vissza

        # Lehetne vizsgálni, hogy Euró e az alap, vagy a cél, és aszerint elágaztatni
        return self.convert_from_eur(self.convert_to_eur(value, base), target)

if __name__ == '__main__':
    c = Converter()
    print(c.convert_from_eur(10, 'HUF'))
    print(c.convert_to_eur(12000, 'HUF'))
    print(c.convert('EUR', 'HUF', 100))
