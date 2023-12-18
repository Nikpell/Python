# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег
MIN_DELTA = 50
ITER_COUNT = 3
COMMISSION_PRESENT = 0.015
COMMISSION_MINIMUM = 30
COMMISSION_MAXIMUM = 600
TAX_LIMIT = 5000000



def check_tax(balance):
    if balance > TAX_LIMIT:
        balance *= 0.9
    return balance

def get_percent(delta):
    commission = delta * COMMISSION_PRESENT
    if commission < COMMISSION_MINIMUM:
        commission = COMMISSION_MINIMUM
    elif commission > COMMISSION_MAXIMUM:
        commission = COMMISSION_MAXIMUM
    return commission


def add_percent(balance):
    return balance * 1.03


def add(balance, count_iter):
    while True:
        delta = input('Введите сумму пополнения: ')
        if delta.isdigit():
            delta = int(delta)
            if delta % MIN_DELTA != 0:
                print('Сумма пополнения должна быть кратной 50 рублей.')
            else:
                break
        else:
            print('Введите число.')
    balance += delta
    count_iter += 1
    if count_iter % ITER_COUNT == 0:
        balance = add_percent(balance)
    return (balance, count_iter)


def get(balance, count_iter):
    while True:
        delta = input('Введите сумму снятия: ')
        if delta.isdigit():
            delta = int(delta)
            commission = get_percent(delta)
            if delta + commission > balance:
                print('Недостаточно денег на счете.')
            elif delta % MIN_DELTA != 0:
                print('Сумма снятия должна быть кратной 50 рублей.')
            else:
                balance -= (delta + commission)
                count_iter += 1
                break
        else:
            print('Введите число.')
    if count_iter % ITER_COUNT == 0:
        balance = add_percent(balance)
    return (balance, count_iter)


def print_summ(balance):
    print(f'На вашем счету {balance} рублей.')


def menu():
    menu_txt = """
    1 - Пополнить
    2 - Снять
    3 - Выйти
    """
    balance = 0
    count_iter = 0
    while True:
        print(menu_txt)
        while True:
            user_input: str = input('Введите номер пункта: ')
            if user_input in ('1', '2', '3'):
                break
        if user_input == '1':
            balance = check_tax(balance)
            balance, count_iter = add(balance, count_iter)
            print_summ(balance)
        if user_input == '2':
            balance = check_tax(balance)
            balance, count_iter = get(balance, count_iter)
            print(f'Bal {balance}')
            print_summ(balance)
        if user_input == '3':
            print_summ(balance)



if __name__ == '__main__':
    menu()