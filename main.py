frontend_input = """amount: 1000000
                    interest: 5.5%
                    downpayment: 20000
                    term: 30"""

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

interest = convert_to_dict['interest']
amount = convert_to_dict['amount']
term = convert_to_dict['term']
downpayment = convert_to_dict['downpayment']

total_amount = amount - downpayment


def monthly_calculator(total, years, interest_ratio):
    interest_ratio = interest / 100
    months = term * 12
    interest_monthly = interest_ratio / 12
    numerator = interest_monthly * ((1 + interest_monthly) ** months)
    denominator = (1 + interest_monthly) ** months - 1
    monthly_payment = float('{0:.2f}'.format(total * numerator / denominator))

    overpay = monthly_payment * months - total_amount

    overall_payment = monthly_payment * months

    return print(f'Месячная выплата по кредиту {monthly_payment}\n'
            f'Общий объем начисленных процентов {overpay}\n'
            f'Общая сумма выплаты {overall_payment}\n')


monthly_calculator(total_amount, term, interest)
