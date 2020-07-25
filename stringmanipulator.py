# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
my_string="This is my home"
print(my_string)

my_list = my_string.split()
back_list = my_list[::-1]
new_string=""

word_count=0
for word in back_list:
    new_string += word + " "
    word_count += 1
    print(word)
    
print(word_count)

print(new_string)

print(range(len(back_list[:])))

for i in range(len(back_list[:])):
    print(i)
    

m_count=0
for word in back_list:
    if "m" in word:
        m_count+=1
print(m_count)


for char in my_string:
    print(char)