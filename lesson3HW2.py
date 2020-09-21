# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Иванов', name='Иван', year='1978', city='Саратов', email='ivanov78@mail.ru',
              telephone='8-903-300-99-87'))
