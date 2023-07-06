triple = lambda x : x*3
length = int(input(" Enter the length of your list : "))
list1 =  []
for _ in range(length):
    temp = int(input("Enter the element : "))
    list1.append(temp)

list2 =list( map(triple,list1))
print("Original list is : ", list1)
print("triple of list is :", list2) 

