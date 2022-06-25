def sum_of_differences(arr):
    # print(max(arr))
    # print(min(arr))
    # print(max(arr) - min(arr)) if arr else 0
    # print(len(arr))
    if (len(arr)) <= 1 or arr == arr.sort(reverse=True):
        print(0)
    else:
        arr.sort(reverse=True)
        i=0
        s=0
        for n in arr:
            s=s+(arr[i]-arr[i+1])

            i+=1
            if i == len(arr)-1:
                break
        print(s)
    

sum_of_differences([2,5,99,100])   