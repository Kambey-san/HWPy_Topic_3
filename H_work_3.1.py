def div(a, b):
    try:
        a, b = int(a), int(b)
        div_num = a / b
    except ValueError:
        return 'Некорректные данные!'
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'
    return round(div_num, 2)

print(div(input('Введите первое число: '), input('Введите второе число: ')))

