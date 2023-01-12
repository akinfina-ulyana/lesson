"""
Создать новый класс Cat, который имеет все те же атрибуты что и Dog,
только заменить метод bark на meow.
"""
from lesson_08.lib.dog import Dog
from  lesson_08.lib.cat import Cat

if __name__ == "__main__":
    dog = Dog(100, 50, "My dog", 10)
    dog.jump()

    dog.change_name(name="New Name")
    dog.run()
    dog.bark()

    cat = Cat(100, 50, "My Cat", 10)
    cat.meow()