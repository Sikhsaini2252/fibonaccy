str = input("Enter your string here : ")
upper = 0
lower = 0 

for i in str:
       if i.isupper():
         upper = upper + 1
       elif i.islower():
          lower = lower + 1
print("The no. of upper case letter : {}  and The No. of lower case letter are : {}".format(upper,lower))  
