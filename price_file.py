total_price = 0
current_price = 0
age = 0
num = 0
while num < 1:
    num = int(input('Введите количество билетов: '))
    if num < 1:                                        # Защита от дурака
        print('Неправильный ввод')

for i in range(num):
    age = int(input(f'Введите возраст {i + 1}-го посетителя: '))
    if 18 <= age < 25:
        current_price = 990
    elif age >= 25:
        current_price = 1390
    elif 0 <= age < 18:
        current_price = 0
    else:
        print('Неправильно указан возраст! Будет применена полная стоимость.')
        current_price = 1390
    print(f'Стоимость билета {current_price} руб.')
    total_price += current_price

if num > 3:
    total_price *= 0.9
    print(f'\nСтоимость всех билетов со скидкой {total_price} руб.')
else:
    print(f'\nОбщая стоимость {total_price} руб.')