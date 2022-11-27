from io import StringIO
import csv

def task(csvString):

    # Обработка csv-файла
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    out = []
    for row in reader:
        out.append([int(row[0]), int(row[1])])
    print(out)

    # Списки
    r1 = []
    r2 = []
    r3 = []
    r4 = []
    r5 = []

    # Создание списка значений типа прямое управление r1
    for a in range(len(out)):
        if out[a][0] not in r1:
            r1.append(out[a][0])

    # Создание списка значений типа прямое подчинение r2
    for a in range(len(out)):
        if out[a][1] not in r2:
            r2.append(out[a][1])

    # Создание списка значений типа опосредованое управление r3
    for a in range(len(out)):
        for y in range(len(out)):
            if out[a][0] not in r3 and out[a][1] == out[y][0]:
                r3.append(out[a][0])

    # Создание списка значений типа опосредованое подчинение r4
    for a in range(len(out)):
        for y in range(len(out)):
            if out[y][1] not in r4 and out[a][1] == out[y][0]:
                r4.append(out[y][1])

    # Создание списка значений типа соподчинение r5
    for a in range(len(out)):
        for y in range(len(out)):
            if out[a][1] not in r5 and out[a][0] == out[y][0] and out[a][1] != out[y][1]:
                r5.append(out[a][1])

    return [r1, r2, r3, r4, r5]

