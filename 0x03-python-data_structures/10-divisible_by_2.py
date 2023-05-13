#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_multiples.append(True)
        else:
            new_multiples.append(False)
    return (new_multiples)
