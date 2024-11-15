#1
def print_params(a=1, b='string', c=True):
    print(a, b, c)
print_params(b=25) # работает, но вместо 'string' будет 25
print_params(c=[1,2,3]) # работает, но вместо True будет список [1,2,3]

#2
values_list = [1, 'word', True]
values_dict = {'a': 2, 'b': True, 'c': 'words' }

print_params(*values_list)
print_params(**values_dict)

#3
values_list_2 = [1.5, 'new_word']
print_params(*values_list_2, 42)

#Ившин Павел