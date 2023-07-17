#CHALLANGE - 1  SQUARE NUMBERS AND RETURN THEIR SUM

class point:
    def _init_(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def sqsum(self):
        print('sum of squared numbers:',self.x*2 , self.y*2 , self.z*2)
x = int(input())
y = int(input())
z = int(input())
obj = point(x,y,z)
print(obj.sqsum())


#CHALLANGE - 2  IMPLEMENT A CALCULATOR CLASS

class calculator:
    def _init_(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num2 - self.num1
    def multiply(self):
       return self.num1 * self.num2
    def divide(self):
        return self.num1 % self.num2
object_1 = calculator(10,94)
print('addition of num1 and num2:',object_1.add())
print('subtraction of num1 and num2:',object_1.subtract())
print('multipication of num1 and num2:',object_1.multiply())
print('division of num1 and num2',object_1.divide())


#CHALLANGE - 3  IMPLEMENT THE COMPLETE STUDENT CLASS

class Student:
    def init(self):
        self.__name = None
        self.__rollNumber = None
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber
    def getRollNumber(self):
        return self.__rollNumber
name = input()
rollnumber = int(input())
student = Student()
student.setName(name)
student.setRollNumber(rollnumber)
name = student.getName()
rollNumber = student.getRollNumber()
print("Name:", name)
print("Roll Number:", rollNumber)

#CHALLANGE - 4  IMPLEMENT A BANKING ACCOUNT

class Account:
    def _init_(self,title,balance):
        self.title = title
        self.balance = balance
class savingsaccount(Account):
    def _init_(self,title,balance,interest_rate):
        super()._init_(title,balance)
        self.interest_rate = interest_rate
title = input()
balance = int(input())
interest_rate = int(input())
account_2 = savingsaccount(title,balance,interest_rate)
print("account title:",account_2.title)
print("account balance:",account_2.balance)
print("account interest",account_2.interest_rate)




#CHALLANGE - 5  HANDLING A BANK ACCOUNT

class account:
    def _init_(self,balance):
        self.balance = balance
    def getbalance(self):
        return self.balance
    def deposit(self,amount):
        self.balance += amount
    def withdrawal(self,amount):
        self.balance -= amount

class savingsaccount(account):
    def _init_(self,balance,interestrate):
        super()._init_(balance)
        self.interestrate = interestrate
    def interestAmount(self):
        return self.balance * (self.interestrate/100)
balance = int(input())
deposit = int(input())
balance_2 = int(input())
withdrawal = int(input())
account_1 = account(balance)
account_1.deposit(deposit)
interest_rate = int(input())
print('deposit of amount:',account_1.getbalance())
account_2 = account(balance_2)
account_2.withdrawal(withdrawal)
print('remaining amount:',account_2.getbalance())
account_interest = savingsaccount(balance_2,interest_rate)
print('total interest:',account_interest.interestAmoun
