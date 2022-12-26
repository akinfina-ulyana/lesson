"""
Пользователь вводит с клавиатуры числа до тех пор, пока не введет любой строчный символ,
из этих чисел составляется первый список. Далее таким же образом вводятся второй и третий списки.
Вывести на экран список, элементы которого есть в первых двух списках, но отсутствуют в третьем.

"""

my_dict = {0: [], 1: [], 2:[]}

for index, lst in my_dict.items():
    while True:
        current_sumbol = input()
        if current_sumbol.isnumeric():
            lst.append(current_sumbol)
        else:
            break

all_elements = set(my_dict[0] + my_dict[1] + my_dict[2])
new_list = []
for element in all_elements:
    if element in my_dict[0] and element in my_dict[1] and element not in my_dict[2]:
        new_list.append(element)

print(new_list)
