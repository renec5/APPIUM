def return2largesNumber(arreglo):
    # n = [ 3,4,5,6,7,4,3,4,665,54,45,34,90]
    n = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    sort = sorted(n)
    large = len(sort)
    menor = 2
    ultimo = 1
    flag = 0
    if (large > 2) and (large >= 3):
        res = sort[large - menor]
        for i in range(large):
            if ((sort[large - menor]) < (sort[large - ultimo])) and ((sort[large - menor]) != (sort[large - ultimo])):
                print("{} is the second largest number on the array".format(sort[large - menor]))
                break
            elif (sort[large - menor] == sort[0]) and (sort[large - menor] == sort[large - ultimo]):
                print("there is no largest second number")
                break
            else:
                menor += 1
                ultimo += 1
    elif (large == 2) and (sort[0] < sort[1]):
        print("{} is the second largest number on the array".format(sort[0]))
    elif large < 2:
        print("There should be at least 2 numbers in the array")
