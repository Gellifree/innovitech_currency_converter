import file_handler

class Converter():
    def __init__(self):
        self.fh = file_handler.FileHandler()

    def convertFromEur(self, value, target):
        return value * self.fh.readExchange()['rates'][target]

    def convertToEur(self, value, base):
        return value / self.fh.readExchange()['rates'][base]

    def convert(self, base, target, value):
        # Konvertáljuk át az értéket, a kiinduló alapból (base) Euróba
        # Az euróban megkapott értéket konvertáljuk át a cél típusba (target)
        # Majd adjuk vissza

        # Lehetne vizsgálni, hogy Euró e az alap, vagy a cél, és aszerint elágaztatni
        return self.convertFromEur(self.convertToEur(value, base), target)

if __name__ == '__main__':
    c = Converter()
    print(c.convertFromEur(10, 'HUF'))
    print(c.convertToEur(12000, 'HUF'))
    print(c.convert('EUR', 'HUF', 100))
