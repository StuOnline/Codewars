def multiple_of_index(arr):
    result =[]
    if len(arr) > 1:
        i = 1
        for item in arr[1::]:
            if ((item/i) == (item//i)):
                result.append(item)  
            i+=1
        print(result)    





multiple_of_index([22, -6, 32, 82, 9, 25])


# def multiple_of_index(l):
#     return [l[i] for i in range(1, len(l)) if l[i] % i == 0]



#     