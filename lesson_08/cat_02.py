from lesson_08.lib.animal import Animal

class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meing")


if __name__ == "__main__":
    cat = Cat(100, 50, "My cat", 10)
    cat.jump()

    cat.change_name(name="Marina")
    cat.run()

    cat.meow()
