def Pol(num):
    a = int(num)
    b = []
    c = 0
    e = 0
    while a > 0:
        c = a % 10
        b.append(c)
        a = a // 10
    d = len(b)
    for i in range(d//2):
        if b[i] == b[d - i - 1]:
            e += 1

    if e == d//2:
        print("YES")
    else:
        print("NO")

Pol(input())
