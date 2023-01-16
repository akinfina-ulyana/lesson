from lesson_08.homework_01_02 import Car

if __name__ == "__main__":
    car = Car("Mercedes", "E500", 2000)

    while car.speed < 100:
        car.speed_plus5()
        print("Km/h")
        car.speed_display()
