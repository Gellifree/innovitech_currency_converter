import file_handler

class ErrorHandler():
    def validCurrency(self, currency):
        self.fh = file_handler.FileHandler()
        data = self.fh.readSymbols()['symbols']
        for curr in data:
            if(curr == currency.upper()):
                return True
        return False

    def validDate(self, date):
        # implement later
        return False


if __name__ == '__main__':
    er = ErrorHandler()
    er.validCurrency('usd')
