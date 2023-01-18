"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds.
Методы: переопределить магические методы сравнения (==, !=, >=, <=, <, >).

Переопределить магические методы сложения, вычитания, умножения на число.

Создать метод, который выводит на экран отформатированное время (HH:MM:SS).

Создать объект класса MyTime, умножить его на 2 и вывести на печать результат.

Создать второй объект класса MyTime, найти разницу с первым,
добавить к нему 7 часов и 45 минут, вывести на печать результат.

Добавить новый класс MyDateTime унаследованный от MyTime. В конструктор добавить
новые атрибуты: day, month, year. “Исправить” все магические методы для этого класса.

Создать объект класса MyDateTime, умножить его на 2 и вывести на печать результат.
"""

class MyTime:
    hours = None
    minutes = None
    seconds = None

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __eq__(self, other):
        return (
            self.hours == other.hours and
            self.minutes == other.minutes and
            self.seconds == other.seconds
        )

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)




if __name__ == "__main__":
    time1 = MyTime(12, 12,12)
    time2 = MyTime(12, 22, 12)

    print(time1 == time2)



    def __init__(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds
        self.timestamp = seconds + minutes * 60 + seconds * 60 * 60




