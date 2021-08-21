from currency.file_handler import FileHandler

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
        if(len(date) < 10):
            return False
        if(date[4] != '-' or date[7] != '-'):
            return False
        return True


    @staticmethod
    def slice_input(input):
        result = []
        slice = ""
        for i in input:
            if(i == " "):
                result.append(slice)
                slice = ""
            else:
                slice += i
        result.append(slice)
        if(len(result) < 2):
            result.append('')
        return result

    @staticmethod
    def recognise_currency(input):
        result = [input, 'unknown']
        # expected input: "121311.131 huf"
        if(ErrorHandler.valid_number(input) == False):
            sliced_result = ErrorHandler.slice_input(input)
            if(ErrorHandler.valid_number(sliced_result[0])):
                result[0] = sliced_result[0]
            else:
                result[0] = "not_valid"
            if(ErrorHandler.valid_currency(sliced_result[1].upper())):
                result[1] = sliced_result[1].upper()
            else:
                result[1] = "not_valid"
        return result

    @staticmethod
    def valid_number_with_currency(number):
        data = ErrorHandler.recognise_currency(number)
        if(data[0] == "not_valid" or data[1] == "not_valid"):
            return False
        return True
