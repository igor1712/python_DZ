"""Возьмите задачу о банкомате из семинара
2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список."""


user_maney: int | float = 0
user_machine_maney: int | float = 1_000_000
machine_maney: int | float = 5_000_000_000_000
count_operation: int = 0
lst_oper = []


def percentage_one_operation(count_maney) -> float:
    global count_operation
    if count_operation <= 3:
        print("Комиссия 1.5 % ")
        return count_maney / 100 * 1.5
    elif count_operation > 3:
        print("Комиссия 3.0 % ")
        return count_maney / 100 * 3.0
    elif count_operation > 5_000_000_0:
        print("Комиссия 10 % ")
        return count_maney / 100 * 10


def add_operation(text: str):
    global count_operation, lst_oper
    lst_oper.append(text)
    count_operation += 1
    print(lst_oper)


def print_balance(user_machine_maney):
    print(f"на вашем счету: {user_machine_maney:.2f} наличными: {user_maney:.2f}")


def take_off_maney():
    global machine_maney, user_maney, user_machine_maney
    count_maney = int(input("Введите сумму: "))
    if machine_maney > count_maney:

        user_maney += count_maney
        machine_maney -= count_maney
        user_machine_maney -= count_maney
        user_machine_maney -= percentage_one_operation(count_maney)
        add_operation(f"Снял {count_maney} ")
        print_balance(user_machine_maney)

    else:
        print("не достаточно средств... ")


def replenish_maney():
    global machine_maney, user_maney, user_machine_maney
    count_maney = int(input("Введите сумму: "))
    if user_maney >= count_maney:
        user_machine_maney += count_maney
        machine_maney += count_maney
        user_maney -= count_maney
        print_balance(user_machine_maney)
        add_operation(f"Пополнил {count_maney} ")
    else:
        print("У вас нет такой суммы")


def machine():
    global machine_maney, user_maney, user_machine_maney
    start = True
    while start:
        print("1. Снять деньги \n2. Пополнить баланс \n3. завершить работу ")
        num = int(input("...-> "))
        match num:
            case 1:
                take_off_maney()
            case 2:
                replenish_maney()
            case 3:
                print("Работа завершена...")
                start = False


machine()

