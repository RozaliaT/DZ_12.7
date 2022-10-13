full_price = 0
while True:
    try:
        tickets = input('Сколько билетов вы хотите купить?:')
        tickets = int(tickets)
        if type(tickets) == int:
            break
    except ValueError:
        print('Только целое число')
for i in range(tickets):
    i += 1
    while True:
        try:
            age = input(f'Для какого возраста билет №{i}? :')
            age = int(age)
            if age < 18:
                print('Билет бесплатный')
            elif 25 > age >= 18:
                full_price += 990
                print('Стоимость билета: 990 руб.')
            else:
                full_price += 1390
                print('Стоимость билета: 1390 руб.')
            if type(age) == int:
                break
        except ValueError:
            print('Только целое число')
if tickets > 5:
    full_price = full_price - ((full_price / 100) * 20)
    print(f'Сумма к оплате {full_price} руб. с учетом 20%-ой скидки на полную стоимость заказа за регистрацию больше 5-и человек')
else:
    print(f'Сумма к оплате {full_price} руб.')