def func(list1, list2):
    mylist = []
    for i in list1:
        flag = False
        for j in list2[i:]:
            if j > i:
                mylist.append(j)
                flag = True
                break
        if flag == False:
            mylist.append(-1)
    return mylist


print(func([4, 1, 2], [1, 3, 4, 2]))
