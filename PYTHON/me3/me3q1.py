"""
Write a Python program to implement Bank Account System:
Implement a BankAccount class that represents a bank account. It should have attributes like account 
number, balance, and owner's name. Methods can include deposit, withdraw, and display balance.
"""
import random
class BankAccount:
    def __init__(self,bal,name):
        self.accountNo = random.randint(11111,99999)
        self.accountBalance = bal
        self.accountOwnerName = name
    def deposit(self,bal):
        if bal>0:
            self.accountBalance += bal
            print(bal,'Amount Deposited\nNew Balance =',self.accountBalance)
        else:
            print('ERROR')
    def withdraw(self,bal):
        if bal<self.accountBalance and bal>0:
            self.accountBalance -= bal
            print(bal,'Amount Withdrawn\nNew Balance =',self.accountBalance)
        else:
            print('ERROR')
    def display(self):
        print('Account No :',self.accountNo)
        print('Account Owner :',self.accountOwnerName)
        print('Account Balance :',self.accountBalance)
userName = input('Enter your Name : ')
userDeposit = int(input('Enter your Initial Deposit : '))
userBankAccount = BankAccount(userDeposit,userName)
while True:
    choice = int(input('\n1.Deposit\n2.Withdraw\n3.Display Balance\n*.Exit\nchoice='))
    if choice not in range(1,4):
        break
    else:
        if choice == 1:
            bal = int(input('Enter Balance to deposit : '))
            userBankAccount.deposit(bal)
        elif choice == 2:
            bal = int(input('Enter Balance to withdraw : '))
            userBankAccount.withdraw(bal)
        if choice == 3:
            userBankAccount.display()