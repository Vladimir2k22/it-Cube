m = float(input("введите свой вес :"))
r = float(input("введите ваш рост в метрах:"))
a = float(r ** 2) // m
if 18.5 < a < 25:
    print("ваш вес в норме:")
elif a < 18.5:
    print("ваш вес низкий:")
else:
    print("ваш вес выше нормы:")
