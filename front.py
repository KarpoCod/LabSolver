import back

end = False
while not end:
    print('0 - инструкция по применению\n1 - 5-я лабораторная \n2 - 6-ая лабораторная \n3 - выход')
    choice = str(input())
    sp = [0, 1, 2, 3]
    if not choice.isdigit():
        print('Введите число от 0 до 3')
    else:
        if int(choice) == 0:
            print('Добро пожаловать в LabSolver!')
            print('Эта программа поможет вам сэкономит время на вычислениях погрешностей.')
            print('Для вычисления значений введите указанные величины.')
            print('Все буквы аналогичны буквам в обычной физике.')
            print('Символы d_, w_ означают абсолютную (дельта) и относительную погрешности величины.')
            print('ВНИМАНИЕ: не вводите нули - это приведёт к поломке программы.')
            print('Если данные отсутствуют, вводите максимально приближенные к нулю значения (0.000000001) или 1.')
            print('Удачи при сдаче!')
            input('Enter для продолжения')
        elif int(choice) == 1:
            print('Открыта 5-я лабораторная работа')
            back.lab_work_5()
        elif int(choice) == 2:
            print('Открыта 6-я лабораторная работа')
            back.lab_work_6()
        elif int(choice) == 3:
            end = True
        else:
            print("nй или угораешь?")
            print("######################################################################################")

print('Хорошего дня!\nСпасибо, что выбрали нашу компанию!')
print('Над проектом работали:\nAlek\nKarppix')
