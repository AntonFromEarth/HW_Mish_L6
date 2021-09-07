'''
Домашнє завдання від 6.09.2021:
1. Написати функцію, яка отримуватиме як агрументи список цілих чисел numbers і ціле числе p, 
 та повертає новий список, де кожен елемент дорівнює відповідному елементу з початкового списку у ступіні p.

'''

def power_list (out_list, power_number):
    if type(out_list) is not list:
        print("It is not list!")
        return
    else:
        return [pow(power_number, a) for a in out_list]
        

my_list = [2, 3, 5, 6, 9]
my_power_num = 2

powered_list = power_list(my_list, my_power_num)

print("List Befor powering: ", my_list)
print("List After powering: ", powered_list)