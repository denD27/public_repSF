per_cent = {
    'bank1': 5,
    'bank2': 10,
    'bank3': 15
}

deposit = int(input('Сколько хотите положить под процент?\n'))
deposits = []
for percent in per_cent.values():
    deposits.append(deposit * (100 + percent) / 100)
print(deposits)


response = 'За год в данных банках вы накопите:\n'
for bank, percent in per_cent.items():
    response += f'{bank}: {deposit + deposit * percent / 100}\n'
print(response)