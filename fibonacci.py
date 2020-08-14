#!/usr/bin/env python
# coding: utf-8

# In[4]:


number = int(input("Please enter the number range: "))

first_number = 0
second_number = 1

for sequence in range(0, number):
    if(sequence <= 1):
        fibonacci = sequence
    else:
        fibonacci = first_number + second_number
        first_number = second_number
        second_number = fibonacci
    
    print(fibonacci)

