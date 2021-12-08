def calculate(m: int, n:int, p:list[int]):
    try:
        if m != n or m != len(p):
            print('Неверные входные данные!')
            return None
        else:
            maxp = sum(p) #сумма всех бонусов без пропуска
            skip = 1 #номер пропускаемого уровня
            while skip != n:
                sum2 = 0 #сумма бонусов с пропусками
                j = 0 #текущий уровень участника
                for i in range(n):
                    if j != skip:
                        sum2 += p[j]
                        j += 1
                    else:
                        j = 0
                    if sum2 > maxp:
                        maxp = sum2
                skip += 1
            print(maxp)
            return maxp
    except TypeError:
        print('Неверный тип входных данных!')
        return None

# calculate(5,5, [8,6, 1,2,3])
# calculate(3,3, [6,2,3])
# calculate(3,3, [2,4,8])