# ask for number
num_digits_mod = list()

num = input('insert a number ')

# split the number
num_digits = [int(d) for d in str(num)]
print(num_digits)

# add one to each number
for i in range(len(num_digits)):
    if num_digits[i] == 9:
        num_digits_mod.append(1)
        num_digits_mod.append(0)
    else:
        num_digits_mod.append(num_digits[i] + 1)

str_digits = [str(x) for x in num_digits_mod]

# print the final number
final_number = ''
for str_d in str_digits:
    final_number = final_number + str_d

print(final_number)
