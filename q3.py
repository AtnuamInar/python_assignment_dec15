#!/usr/bin/python3
num_list = [1, 2, 3, 4, 6, 7, 8, 9]


def power(num_list):
    cube = list();
    for num in num_list:
        cubed = num ** 3
        cube += [cubed]

    return cube


cube = power(num_list)

print('Original list\t = {}\nCubed list\t = {}'.format(num_list, cube))

