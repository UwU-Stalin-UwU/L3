print ('Добрый день! Введите имя, по которому к Вам можно обратиться:')
a=input()
print ('Добрый день, ' + a + '! Введите ваш возраст, и я посчитаю, сколько Вам осталось до пенсии в годах:')
b=input()
b=int(b)
b=63-b
b=str(b)
print('Вам до пенсии осталось: ' + b + ' лет. Всего доброго')