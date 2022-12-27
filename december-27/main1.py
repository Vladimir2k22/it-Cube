a, b, c = int(input()), int(input()), int(input())
if a == b:
    print(2)
elif a == b and a == c:
    print(3)
elif a != c and c != b:
    print(0)