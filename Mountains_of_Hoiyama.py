

def mountains_of_hoiyama(width):
    row = (width+1)//2
    mount = [[a for a in range(b + 2)] for b in range(1,width,2)]
    cent = [a for a in range(len(mount)+1,width)]

    step =[[a for a in range((x-1),x)]for x in cent[::-1]]
    st = [item for i in step for item in i]
    res = [ [a for a in range(st[x]-x,st[x]+1)] for x in range(len(st))]
    st2 = [item for i in res for item  in i*2]
    s = width + sum(cent) + sum(st2)

    #def mountains_of_hoiyama(w):
        #return ((width + 1) ** 3 - width ** 2) // 8 + 1



mountains_of_hoiyama(9)  