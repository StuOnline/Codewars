def warn_the_sheep(queue):
    sheep_count = len(queue)
    wolf_id = sheep_count - queue.index('wolf')

    print(wolf_id)
    
 

    # print(queue.index('wolf')
    # # if quene.find('wolf')==quene.count()
warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep'])

#Интересное решение
# def warn_the_sheep(queue):    
#     queue.reverse()       # перевернул
#     wolfnum = queue.index("wolf")
#     if wolfnum == 0:
#         return "Pls go away and stop eating my sheep"  
#     else:
#         return "Oi! Sheep number {0}! You are about to be eaten by a wolf!".format(wolfnum) # Вставил номер красиво

# Еще одно красивое
# def warn_the_sheep(queue):
#     i = queue[::-1].index('wolf')
#     if i == 0:
#         return 'Pls go away and stop eating my sheep'
#     return f'Oi! Sheep number {i}! You are about to be eaten by a wolf!'
