def _sum(arg):
    i=0
    sum=0
    chislo = ''
    while i != len(arg):
        if arg[i] != ' ':
            chislo += arg[i]
        else:
            sum+=int(chislo)
            chislo=''
        i+=1
    sum += int(chislo)
    return sum

def _mult(arg):
    i=0
    proizv = 1
    chislo = ''
    while i != len(arg):
        if arg[i] != ' ':
            chislo += arg[i]
        else:
            proizv*=int(chislo)
            chislo=''
        i+=1
    proizv *= int(chislo)
    return proizv

def _min(arg):
    i=0
    min=10**9
    chislo = ''
    while i != len(arg):
        if arg[i] != ' ':
            chislo += arg[i]
        else:
            if min >= int(chislo):
                min = int(chislo)
            chislo=''
        i+=1
    if min >= int(chislo):
        min = int(chislo)
    return min

def _max(arg):
    i=0
    max=-10**9
    chislo = ''
    while i != len(arg):
        if arg[i] != ' ':
            chislo += arg[i]
        else:
            if max <= int(chislo):
                max = int(chislo)
            chislo=''
        i+=1
    if max <= int(chislo):
        max = int(chislo)
    return max

a = open('mydata', 'r')
a = a.readline()

print('Приветствуем Вас в многофункциональной программе!')
zadacha = str(input('Какую функции хотите применить к файлу? \n 1 - Минимальное значение; 2 - Максимальное значение \n 3 - Сумма всех чисел; 4 - Произведение всех значений \n'))
if zadacha == '1':
    print(_min(a))
elif zadacha == '2':
    print(_max(a))
elif zadacha == '3':
    print(_sum(a))
elif zadacha == '4':
    print(_mult(a))
else:
    print('Похоже вы выбрали несуществующую функцию...')

