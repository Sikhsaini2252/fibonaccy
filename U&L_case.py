def upper_lower(string):
upper = 0
lower = 0 
for Char in string :
       if Char.isupper():
            upper += 1
       elif Char.islower():
            lower += 1
print("The no. of upper case letter : {}  and The No. of lower case letter are : {}".format(upper,lower))  

temp = input('Enter the string :')
lower(temp) 
