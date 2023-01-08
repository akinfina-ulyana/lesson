"""
Создайте функцию three_args(), которая принимает 1, 2 или 3 ключевых параметра.
В результате ее работы на печать выводятся значения переданных переменных,
но только если они не равны None. Получим, например, следующее сообщение:
Переданы аргументы: var1 = 2, var3 = 10.

"""
def three_args(**kwargs):
   for key, value in kwargs.items():
       print(key, "=", value)

three_args(var1 = 2, var2 = 5, var3 = 10)


"""
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
"""





