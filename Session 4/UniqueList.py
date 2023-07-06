def U_list(arr):
    a = []
    for i in arr:
        if i not in a:
            a.append(i)

    for i in a:
        print(i)

U_list([0,10,4,3,0,-1,3])
