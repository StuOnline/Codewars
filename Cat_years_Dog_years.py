def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 24
        dog_years = 24
    else:
        cat_years = 24 + (human_years - 2) * 4
        dog_years = 24 + (human_years - 2) * 5

    print([human_years, cat_years, dog_years])    
        


human_years_cat_years_dog_years(15)


# def human_years_cat_years_dog_years(x):
#     return [x, 24+(x-2)*4 if (x != 1) else 15, 24+(x-2)*5 if (x != 1) else 15]


# def human_years_cat_years_dog_years(n):
#     cat_years = 15 + (9 * (n > 1)) + (4 * (n - 2) * (n > 2))
#     dog_years = 15 + (9 * (n > 1)) + (5 * (n - 2) * (n > 2))
#     return [n, cat_years, dog_years]