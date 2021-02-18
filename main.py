frontend_input = """amount: 100000 
                    interest: 5.5% 
                    downpayment: 20000
                    term: 30 """

split_input = frontend_input.split('\n')
convert_to_dict = dict(entry.replace('%', '').strip().split(': ') for entry in split_input)

# Проверка является ли строка числом

for key, value in convert_to_dict.items():
    if value.isdigit():
        convert_to_dict[key] = int(value)
    else:
        try:
            if float(value.replace('/', '')):
                convert_to_dict[key] = float(value)
        except ValueError:
            print('Некорректный формат ввода!')

