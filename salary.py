#!/usr/bin/python3
salary = [15000, 20000, 17000, 18900, 30000]

def new_salary(salary):
    return salary+0.23*salary

print('New Slaray: ')
for index, each in enumerate(salary,start=1):
    raised_salary=new_salary(each)
    print('For employee {}, total salary = Rs. {:.2f}'.format(index, raised_salary))

