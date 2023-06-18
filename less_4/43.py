balance = 0
count_operation = 0



def dep(amount):
    global balance, count_operation
    balance += amount
    count_operation += 1
    if count_operation % 3 == 0:
        balance += balance * 0.03
    if balance > 5000000:
        balance -= balance * 0.1
    return f"Текущий баланс: {balance}"


def wit(amount):
    global balance, count_operation
    if amount > balance:
        print("На счете недостаточно средств")
        return
    commission = amount * 0.015 if amount * 0.015 >= 30 else 30
    if commission > 600:
        commission = 600
    balance -= amount + commission
    count_operation += 1
    if count_operation % 3 == 0:
        balance += balance * 0.03
    if balance > 5000000:
        balance -= balance * 0.1
    print(f"Текущий баланс: {balance}")


information_field = """
Действе над счетом
Введите нужное вам действие
1. Пополнение
2. Снятие
0. Выход

Выберите действие \nВвод:
"""
print(information_field)
choice = int(input("Ваш выбор: "))
match choice:
    case 1:
        amount = int(input("Введите сумму для пополнения: "))
        if amount % 50 != 0:
            print("Сумма должна быть кратной 50 у.е.")
        else:
            dep(amount)
    case 2:
        amount = int(input("Введите сумму для снятия: "))
        if amount % 50 != 0:
            print("Сумма должна быть кратной 50 у.е.")
        else:
            wit(amount)
    case 0:
        print("Выход")