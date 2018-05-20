a = 10
b = 15

def UCLN(a, b):
    if b == 0:
        return a
    else:
        return UCLN(b, a % b)

print(UCLN(10, 15))
