def each_cons(lst, n):
    m = (len(lst) - n) + 1
    my_list = []
    for i in range(m):
        my_list.append(lst[i:i+n])
        

               


    print(my_list)




    print(m)
    print(n)
    print(i)



each_cons([3, 5, 8, 13,15],2)







