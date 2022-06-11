def sum_num():
    a = 0
    while True:
        user_list = input('Введите числа, разделённые пробелом, или "q" для выхода: ').split()
        for num in user_list:
            if num == 'q':
                return (a, 'Программа завершена!')
            else:
                try:
                    a += int(num)
                except ValueError:
                    print('Для выхода введите q: ')
        print(f'Сумма равна = {a}')
print(sum_num())
