def sum_dig(num):
    a = 0
    num = int(num)
    while num > 0:
        a += (num % 10)
        num = num // 10
    print(a)

sum_dig(input())
