Text = 'abc-5xyz-10p91--'

def FindNegativeNumber(Text):
    Text = Text + 'aWord'
    Number = ''
    array = list()
    ListNumber = list()

    for i in range(len(Text)):
        if Text[i].isalpha() == False:
            Number = Number + Text[i]
        else:
            array.append(Number)
            Number = ''

    for i in array:
        if i != '':
            ListNumber.append(i)

    for num in ListNumber:
        if (num[0] == '-') and (len(num) > 1):
            print num,

FindNegativeNumber(Text)
