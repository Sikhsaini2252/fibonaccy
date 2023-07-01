#l1 = [8, 2, 3, 0, 7]
#def sum(l1):
 #   for i in l1 :
  #      i += i 
   #     return i
    #print(sum(l1))


numbers = [8, 2, 3, 0, 7]

def sum(numbers):
    total = 0
    for x in numbers :
        total += x
    return total
print (sum(numbers))    