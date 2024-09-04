def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(3, 4, 5)
print_params(7, 8)
print_params(9)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
values_list = (False, 56, 'oba-na')
values_dict = {'a': 'tutu', 'b': False, 'c': 77}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)