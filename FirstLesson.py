per = {'MKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0,}

money = int(input("Введите сумму которую планируете положить под проценты:"))
MKB = int((per['MKB'])*(money/100))
SKB = int((per['SKB'])*(money/100))
VTB = int((per['VTB'])*(money/100))
SBER = int((per['SBER'])*(money/100))

deposit = [MKB, SKB, VTB, SBER]
print("Накопленные средства за год вклада в каждом из банков =",deposit)
print("Максимальная сумма котрую можно будет забрать:", max(deposit))
