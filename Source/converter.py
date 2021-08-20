class Converter:
    @staticmethod
    def convert_from_eur(value, target):
        from file_handler import FileHandler
        return value * FileHandler.read_exchange()['rates'][target]

    @staticmethod
    def convert_to_eur(value, base):
        from file_handler import FileHandler
        return value / FileHandler.read_exchange()['rates'][base]

    @staticmethod
    def convert(base, target, value):


        # Lehetne vizsgálni, hogy Euró e az alap, vagy a cél, és aszerint elágaztatni
        return Converter.convert_from_eur(Converter.convert_to_eur(value, base), target)
