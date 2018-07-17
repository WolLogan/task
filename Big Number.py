Text = '13a7b48cb7b9e68f7'
value = 5
number = ''
array = list()

for i in range(len(Text)):
    if Text[i].isdigit() == True:
        number = number + Text[i]

def GenNumber(length, array):
    start = 0
    while start <= len(number) - length:
            array.append(number[start:start + length])
            start += 1

for i in range(1, len(number)):
    GenNumber(i, array)

def MaxNumber(array):
    max = array[0]
    for i in array:
        if (max <= i) and (len(i) == value):
            max = i
    return max

print MaxNumber(array)
