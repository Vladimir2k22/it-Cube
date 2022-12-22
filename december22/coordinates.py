x = int(input("введите ось x:"))
y = int(input("введите ось y:"))
if x > 0 and y > 0:
    print("1 четверть")
if x < 0 and y > 0:
    print("2 четверть")
if x < 0 and y < 0:
    print("3 четверть")
if x > 0 and y < 0: 
    print("4 четверть")   
