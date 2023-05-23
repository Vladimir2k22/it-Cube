a = input()
b = int(len(a) *100)
b = (b * 60) // 100
g = b // 100
d = b % 100
print(g, "руб", d, "коп")
