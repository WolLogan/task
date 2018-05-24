number = input('Nhap so: ')

def Gen(n):
    String = ''
    for i in range(1, n + 1):
        String = String + str(i)
    return String

number = Gen(number)
print number

def Delete1(number):
    Str = ''
    for i in range(len(number)):
        if i % 2 == 0:
            Str = Str + number[i]
    return  Str

def Delete2(number):
    Str = ''
    for i in range(len(number)):
        if i % 2 != 0:
            Str = Str + number[i]
    return Str

while len(number) > 1:
    if len(number) > 1:
        number = Delete1(number)
        print number
    if len(number) > 1:
        number = Delete2(number)
        print number

print "Result:", number
