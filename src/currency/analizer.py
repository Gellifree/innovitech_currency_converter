from currency.file_handler import FileHandler

class Analizer:
    @staticmethod
    def generate_data():
        result = []
        data_set = FileHandler.read_saved_conversions()
        next(data_set)
        for data in data_set:
            result.append((data[1], data[2]))
        return result

    @staticmethod
    def collect_from_data():
        data_set = Analizer.generate_data()
        
        result = {
            'base' : {},
            'target' : {}
        }

        for data in data_set:
            if(data[0] in result['base']):
                result['base'][data[0]] += 1
            else:
                result['base'][data[0]] = 1

            if(data[1] in result['target']):
                result['target'][data[1]] += 1
            else:
                result['target'][data[1]] = 1
        return result

    @staticmethod
    def calculate_mostly_used():
        currency_list = []
        data_set = Analizer.collect_from_data()
        for data in data_set:
            sorted_var = sorted(data_set[data].items(), key=lambda x: x[1], reverse=True)
            currency_names = []

            for currency_tuple in sorted_var:
                currency_names.append(currency_tuple[0])

            if(len(data_set[data]) <= 5):
                currency_list.append(currency_names)
            else:
                result = []
                for i in range(5):
                    result.append(currency_names[i])
                currency_list.append(result)
        # A lista nulladik eleme, azokat tartalmazza, amikből átváltottunk
        # az első eleme pedig azokat, amikbe átváltottunk
        return currency_list

    @staticmethod
    def calculate_last_five():
        result = [
            [],
            []
        ]
        data = Analizer.generate_data()
        data.reverse()
        for d in data:
            if(len(result[0]) < 5):
                if d[0] not in result[0]:
                    result[0].append(d[0])
            if(len(result[1]) < 5):
                if d[1] not in result[1]:
                    result[1].append(d[1])
        return result
