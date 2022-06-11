def my_func(x, y):
    try:
        x, y = int(x), int (y)
        if x <= 0:
            return 'Х должен быть больше нуля!'
        if y >= 0:
            return 'Y должен быть меньше нуля!'
        else:
            result = 1
            for _ in range(abs(y)):
                result *= 1 / x
            return f'Результат возведения X в степень Y: {round(result, 6)}'
    except ValueError:
        return 'Вводите числа отличные от нуля!'
print(my_func(4, -5))

