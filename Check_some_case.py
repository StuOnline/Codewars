def same_case(a, b): 
    if  a.isalpha() and b.isalpha():
        if a.isupper()==b.isupper():
            print(1)
        else:
            print(0)
    else:
        print(-1)

same_case('-','b')