math_marks = {'Rifat':85, 'Siam': 71, 'Meghla':90, 'Shamim':82}
# max_value = max(math_marks.values())
# print(max_value)

max_key = next(iter(math_marks))

for key in math_marks:
    if math_marks[key]>math_marks[max_key]:
        max_key = key
print(max_key)



