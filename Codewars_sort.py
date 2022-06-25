
def flip(d, a):
    # if d =='R':
    #     print(sorted(a))
    # if d =='L':
    #     print(a.sort(reverse=True))
    print(sorted(a,reverse=d=='L'))
flip('L',[1,4,2,5,7,3])        