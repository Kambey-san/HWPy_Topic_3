def personal_data(**BigBrotherIsWatchingYou):
    return ' '.join(BigBrotherIsWatchingYou.values())

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
birthday = input('Укажите год рождения: ')
place = input('Укажите город проживания: ')
email = input('Укажите Ваш эл. адрес: ')
phone = input('Укажите номер Вашего телефона: ')
print(personal_data(name=name, surname=surname, birthday=birthday, \
                    place=place, email=email, phone=phone))
