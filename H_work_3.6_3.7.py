def int_func(user_text):
    keyboard = 'qwertyuiopasdfghjklzxcvbnm'
    return  user_text.title() if not set(user_text).difference(keyboard) else False
text = input('Введите слова на латинице через пробел c маленькой буквы: ').split()
for a in text:
    result = int_func(a)
    if result:
        print(int_func(a), ' ')