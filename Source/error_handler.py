import file_handler

class ErrorHandler():
    def valid_currency(self, currency):
        self.fh = file_handler.FileHandler()
        data = self.fh.read_symbols()['symbols']
        for curr in data:
            if(curr == currency):
                return True
        return False

    def valid_number(self, number):
        try:
            result = float(number)
            return True
        except:
            return False

    def valid_date(self, date):
        # implement later
        return False


if __name__ == '__main__':
    er = ErrorHandler()
    er.valid_currency('usd')
