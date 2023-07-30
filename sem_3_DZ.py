"""Дан список повторяющихся элементов. Вернуть список с
дублирующимися элементами. В результирующем списке
не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]"""

lst = [1, 2, 3, 1, 2, 4, 5, 5, 6, 6, 9, 9, 10, 10, 11, 11]


def dubl_list(lst):
    new_lst = []
    for i in lst:
        if lst.count(i) > 1:
            new_lst.append(i)
    print(list(set(new_lst)))


"""В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
Не учитывать знаки препинания и регистр символов. 
За основу возьмите любую статью из википедии или из документации к языку.
(Может помочь метод translate из модуля string)"""

text = "Высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим" \
       " управлением памятью, ориентированный на повышение производительности разработчика, читаемости кода и его качества."


def translate_text_func(text):
    tb = {",": "", "!": "", ".": "", " ": "", "?": ""}
    trans_tb = text.maketrans(tb)
    return text.translate(trans_tb)


t_text = translate_text_func(text).lower()


def count_abc(t_text):
    abc_dic = {}
    for i in t_text:
        counter = t_text.count(i)
        abc_dic[counter] = i
    return abc_dic


dict_abc = count_abc(t_text)


def max_abc(dict_abc):
    lst = []

    for key, value in dict_abc.items():
        lst.append(key)
        lst.sort(reverse=True)

    for i, item in enumerate(lst, start=1):
        if i == 11:
            break

        print(f"{i}. {dict_abc.get(item)} --> {item} ")


# max_abc(dict_abc)

"""Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака."""

list_of_things = {
    "Кружка": 0.5, "ложка": 0.1, "вилка": 0.1, "нож": 0.3,
    "одежда": 10, "аптечка": 5,
    "предметы личной гигиены": 5,
    "фонарь": 3,
    "зарядное устройство и адаптер": 2
}


def sum_bag_weight(list_of_things):
    bag_lst = []
    for value in list_of_things.values():
         bag_lst.append(value)
    sum_bag = sum(bag_lst)
    return sum_bag

s_bw = sum_bag_weight(list_of_things)


def max_bag_weight(s_bw):
    MAX_WEIGHT = 30

    if s_bw >= MAX_WEIGHT:
        print(f"У вас перевес сумки в {s_bw - MAX_WEIGHT} ")
    else:
        print("Можно идти в поход")

max_bag_weight(s_bw)
