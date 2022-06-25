def test_from_k(name):
    name_fix=[]           # из строки соберу в список
    repeat = []           # список повторов
    unic =[]              # уникальный (точнее каждого знака по 1 экз)


    for i in name:              # цикл для сбора списков  
        name_fix.append(i)
        if i not in unic:
            unic.append(i)  
        else:
            repeat.append(i)


    for n, i in enumerate(name_fix, 0):  # цикл для проверки первого собранного списка с вспомогательными
        if i in repeat and i in unic:
            name_fix[n]='('               
        else:
            name_fix[n]= ')' 

    print (''.join(i for i in name_fix))   # собираю из списка строку          


test_from_k('qqqqwwwwerty----   nk  jhgfds')

''' Интересная задача ),  алгоритм сразу был понятен, а вот по коду, пришлось повозиться
Я, возможно, скобки не туда завернул, но это поправить можно.

''' 