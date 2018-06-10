String = 'AAABBC'
String = String + ' '
count = 1

for i in range(len(String) - 1):
    if String[i] == String[i + 1]:
        count += 1
    else:
        print count, String[i],
        count = 1
