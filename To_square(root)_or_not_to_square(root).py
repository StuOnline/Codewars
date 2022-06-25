from math import sqrt

def square_or_square_root(arr):
    print ([int(sqrt(a)) if sqrt(a) % 1 == 0 else a ** 2 for a in arr])
    
           








square_or_square_root([4, 3, 9, 7, 2, 1 ])