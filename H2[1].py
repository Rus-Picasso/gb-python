# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

a=int(input('Введите количество секунд: '))
h=((a//3600))%24
m=(a//60)%60
s=a%60
if m<10:
    m=str('0'+str(m))
else:
    m=str(m)

print('чч:', h, 'мм:', m, 'сс:', s)