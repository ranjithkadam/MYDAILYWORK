
# Program for Generating Random Password with Specific Length

import random
import string

#Reading Password Length from User
UserInput = int(input("Enter the Length of the Password "))

# Generating Random String(Password)
alpha = string.ascii_letters
num=string.digits
total = alpha + num
password = ''
 
for i in range(UserInput):
   s=random.choice(total) 
   password =str(password) + s

# Displaying Password   
print("\nRandomly Generated Password is --> ",password)       
