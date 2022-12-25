import csv
import math
from io import StringIO

def parents(array, n):
    count = 0
    for i in range(len(array)):
        if (array[i][1] == n):
            count += 1
    return count

def childs(array, n):
    count = 0
    for i in range(len(array)):
        if (array[i][0] == n):
            count += 1
    return count

def ancestors(array, n):
    count = 0
    for i in range(len(array)):
        if (array[i][0] == n):
            count += 1
            count += ancestors(array, array[i][1])
    return count

def descendants(array, n):
    count = 0
    for i in range(len(array)):
        if (array[i][1] == n):
            count += 1
            count += descendants(array, array[i][0])
    return count

def siblings(array, n):
    count = 0
    parent = 0
    for i in range(len(array)):
        if (array[i][1] == n):
            parent = array[i][0]
            break
    for i in range(len(array)):
        if (array[i][0] == parent):
            count += 1
    return count - 1 if count > 0 else 0

def task(csvString):

    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    array = []

    for row in reader:
        array.append(row)

    array1 = []

    for i in range(len(array)):
        repet = 0
        for k in range(len(array1)):
            if (array1[k] == array[i][0]):
                repet = 1
                break
        if (not repet):
            array1.append(array[i][0])
    for i in range(len(array)):
        repet = 0
        for k in range(len(array1)):
            if (array1[k] == array[i][1]):
                repet = 1
                break
        if (not repet):
            array1.append(array[i][1])

    array3 = []

    counts = [[0, 0]]

    for k in range(len(array1)):
        name = array1[k]
        parent = parents(array, name)
        child = childs(array, name)
        ancestor = ancestors(array, name)
        descendant = descendants(array, name)
        sibling = siblings(array, name)
        array3.append([name, [child, parent, ancestor - child, descendant - parent, sibling]])

    for k in range(len(array1)):
        for i in range(5):
            value = array3[k][1][i]
            repet = 0
            index = 0
            for j in range(len(counts)):
                if (counts[j][0] == value):
                    index = j
                    repet = 1
                    break
            if (repet == 0):
                counts.append([value, 1])
            else:
                counts[index][1] += 1

    result = 0
    n = len(array1)

    for k in range(1, len(counts)):
        v = (counts[k][0] / (n - 1))
        result -= counts[k][1] * (v * math.log2(v))

    return result














