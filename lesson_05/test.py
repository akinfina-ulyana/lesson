

def three_args(*args, **kwargs):
    result = []
    for key, value in kwargs.items():
        if value is not None:
            result.append(f"{key} = {value}")
    print(f"Переданы аргументы: {', '.join(result)}")


print(three_args(var1=2, var3=10))
