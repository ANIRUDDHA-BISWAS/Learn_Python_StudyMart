# frequency count

my_tuple = (1,2,3,4,1,2,3,1,2,1)
frequency_dict = {}

for num in my_tuple:
    if num in frequency_dict:
        frequency_dict[num] += 1
    else:
        frequency_dict[num] = 1
print(frequency_dict)