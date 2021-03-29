print('='*5, 'Рассчитать вклад', '='*5)

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
list_of_banks = print('Мы работаем с банками: ',list(per_cent.keys()))

money = int(input('Введите размер годового вклада'))

deposit = list(map(int, [per_cent['ТКБ']*(money/100), per_cent['СКБ']*(money/100), per_cent['ВТБ']*(money/100), per_cent['СБЕР']*(money/100)]))
print('Максимальная сумма, которую вы можете заработать - ', max(deposit))

