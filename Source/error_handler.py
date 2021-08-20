from file_handler import FileHandler

class ErrorHandler:
    @staticmethod
    def valid_currency(currency):
        data = FileHandler.read_symbols()['symbols']
        for curr in data:
            if(curr == currency):
                return True
        return False

    @staticmethod
    def valid_number(number):
        try:
            result = float(number)
            return True
        except:
            return False

    @staticmethod
    def valid_date(date):
        # implement later
        return False
