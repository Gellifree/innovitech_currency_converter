import file_handler

class ErrorHandler():
    def validCurrency(self, currency):
        self.fh = file_handler.FileHandler()
        data = self.fh.read_symbols()['symbols']
        for curr in data:
            if(curr == currency.upper()):
                return True
        return False


if __name__ == '__main__':
    er = ErrorHandler()
    er.validCurrency('usd')
