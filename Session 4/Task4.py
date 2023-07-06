def _(st):
    y_set=[]
    arr = {}
    for i in st:
        y_set.append(i)

    for j in y_set:
        a = 0
        for i in st:
            if i == j:
                a += 1
             
        if a > 1:
             arr[j] = a
    print(arr)

_(input())    


