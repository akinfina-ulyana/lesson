"""
Создать функцию, которая принимает на вход неопределенное
количество аргументов и возвращает их сумму и максимальное из них.
"""

def sum_and_max(*args):
    my_sum = 0
    my_min = args[0]
    for element in args:
        my_sum += element
        if element > my_min:
            my_min = element
    return my_sum, my_min

print(sum_and_max(1, 2, 5, 8, 3, 2))


#def sum_and_max_2(*args):
#    return sum(args), min(args)

