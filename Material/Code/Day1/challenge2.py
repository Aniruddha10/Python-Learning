my_string = "All good things must end"

my_list = my_string.split()
print(my_list)
back_list = my_list[::-1]
print(back_list)
new_string = ""
for word in back_list:
    new_string += word + " "

print(new_string)

for i in range(len(my_list)):
    my_list[i] = my_list[i][::-1]

print(my_list)
new_string = ""
for word in my_list:
    new_string += word + " "

print(new_string)
print(my_string, 12 + 34)

count = 0
for word in my_list:
    if "g" in word:
        count +=1
print(count)

for char in my_string:
    print(char + "\n")