def multi_table(number):
    out = ""
    for num in range(1,11):
        out += (str(num) + " * " + str(number) + " = " + str(num * number ) + "\n")
    print(out.strip())




multi_table(5)


