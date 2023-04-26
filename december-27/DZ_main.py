s = input()
n = 'Цифр нет'
for i in range(len(str(s))):
    if s[i] in '0123456789':
        n = 'Цифра'
        break
print(n)