#!/usr/bin/python3
def name():
    full_name=input('Enter you full name: ')
    return full_name.split(" ")

temp=name()
if (len(temp)==3):
    first_name, middle_name, last_name=temp
    print('First name:\t{}\nMiddle name:\t{}\nLast name:\t{}'.format(first_name, middle_name, last_name))

else:
    first_name , last_name = temp
    print(first_name,last_name)
