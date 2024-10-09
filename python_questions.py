#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q-1
vow = "aeiouAEIOU"

def is_vowel(char):
    if char in vow:
        return True
    else:
        return False
char = input("Enter a character: ")

if is_vowel(char):
    print(f"'{char}' is a vowel.")
else:
    print(f"'{char}' is not a vowel.")


# In[3]:


#Q-2
def calculate_fee(days):
    fee = 0
    if days <= 5:
        fee = days * 2
    elif days <= 10:
        fee = (5 * 2) + ((days - 5) * 3)
    elif days <= 15:
        fee = (5 * 2) + (5 * 3) + ((days - 10) * 4)
    else:
        fee = (5 * 2) + (5 * 3) + (5 * 4) + ((days - 15) * 5)
    return fee

days = int(input("Enter the number of days the book is used: "))

if days > 0:
    total_fee = calculate_fee(days)
    print(f"The total fee for {days} days is: Rs. {total_fee}")
else:
    print("Invalid input. Days must be a positive number.")


# In[ ]:


#Q-3
def check_weirdness(n):
    if n % 2 != 0:
        print("WEIRD")
    elif n % 2 == 0:
        if 2 <= n <= 5:
            print("NOT WEIRD")
        elif 6 <= n <= 20:
            print("WEIRD")
        elif n > 20:
            print("NOT WEIRD")
            
n = int(input("Enter a positive integer: "))

if n > 0:
    check_weirdness(n)
else:
    print("Invalid input. Please enter a positive integer greater than 0.")

