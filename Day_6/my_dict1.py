my_dict = {'a':1, 'b':2, 'c':3}
key_remove = 'b'

if key_remove in my_dict:
    del my_dict[key_remove]
print(my_dict)