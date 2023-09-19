#приветствие
print('Добро пожаловать в калькулятор!')

#запись первого числа
while True:
    first_value = input('Введите первое число:')
    second_value = input('Введите второе число:')
    if first_value.isnumeric() and second_value.isnumeric():
        break
    else:
        print('Введите пожалуйста число!')

#доступные операции
operations = {1: 'умножение', 2: 'деление', 3: 'сложение', 4: 'вычитание', 5: 'возведение в степень'}
output = ''
for key, value in operations.items():
    output += f'{key} - {value}, '
output = output[:-2]

#выбор операции
while True:
    op = input('Введите пожалуйста номер операции:\n' + output)
    if op.isnumeric():
        op = int(op)
        if op >= 1 and 5 >= op:
            break
    else:
        print('Yет такой операции')

#вычисления
def calculations(fv, sv):
    fv, sv = int(fv), int(sv)
    if op == 1:
        return fv * sv
    if op == 3:
        return fv + sv
    if op == 4:
        return fv - sv
    if op == 5:
        return fv ** sv
    else:
        fv, sv = float(fv), float(sv)
        return fv / sv

#выводим результат
print('Результат расчетов:', calculations(first_value, second_value))