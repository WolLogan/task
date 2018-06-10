Brackets = '{}'
count = 0

if len(Brackets) % 2 == 0:
    for i in range(len(Brackets)):
        if (Brackets[i] == '(') or (Brackets[i] == '[') or Brackets[i] == '{':
            count += 1
        if (Brackets[i] == ')') or (Brackets[i] == ']') or (Brackets[i] == '}'):
            count -= 1
    if count == 0:
        print True
else:
    print False
