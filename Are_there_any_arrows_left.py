def any_arrows(quiver):
    for arrow in quiver:
        print(arrow.get('damaged')!= True)
        
        # if (arrow.get('range') is True or None) or not arrow.get('damaged'):
                # print(True)
    # print(False)






any_arrows([{'range': 5}, {'range': 10, 'damaged': True}, {'damaged': True}])      