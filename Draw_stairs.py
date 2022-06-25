def draw_stairs(n):
    # string = ''
    # for num in range(0,n-1):
    #     string += ' '*num + 'I\n'
    # string +=  ' '*(n-1) + 'I'
    # print(string)
	print('...'.join(str(i+1) +'sheep' for i in range(n)))

draw_stairs(2)


# короткое решение
# return '\n'.join(' '*i+'I' for i in range(n))

# "1 sheep...2 sheep...3 sheep..."