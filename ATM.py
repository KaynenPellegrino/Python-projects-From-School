
import sys

#account balance 
account_balance = float(500.25)


#<--------functions go here-------------------->
#balance functions, as well as defining the function
def printbalance():
    print('Your  current balance:')
    return account_balance
#deposit functions, as well as defining the function
def deposit():
    deposit_amount = float(input("How much would you like to deposit today?\n"))
    balance = account_balance + deposit_amount
    print("Deposit was $%.2f, current balance is $%.2f" %(deposit_amount, balance)) #%.2f uses % to call the number, .2f floating
#deposit functions, as well as defining the function
def withdraw():
    withdraw_amount = float(input("How much would you like to withdraw today?\n"))
    if(withdraw_amount > account_balance):
        print("$%.2f is greater than your account balance of $%.2f" %(withdraw_amount,account_balance)) #%.2f uses % to call the number, .2f floating
    else:
        balance = account_balance - withdraw_amount
        print("Withdrawal amount was $%.2f, current balance is $%.2f" % (withdraw_amount, balance)) #%.2f uses % to call the number, .2f floating

keep_going = True #I found a command that would allow the program to Loop until Q was entered.

while keep_going: 
        
  userchoice = input ("What would you like to do?\n") #begins the selection process

  while(userchoice != 'D') and (userchoice != 'W') and (userchoice !='B') and (userchoice !='Q'):
      userchoice = input("Please type a valid response.\n Would you like to deposit(D), withdraw(W), your balance(B), or to quit(Q)?\n")
    #In order to keep people on the right track, i wrote a line so that the program would only proceed with the correct inputs, or else the user would be told what inputs are valid.
  if (userchoice == 'D'):
      deposit()
#      account_balance += deposit()
#here I tried to make the account balance update with the new amount after deposit, but I couldn't seem to figure out the coding that would work.
  elif userchoice == 'W':
      withdraw()
#      account_balance -= withdraw()
#Here I tried to make the account balance update with the new amount after withdrawal, but like the deposit, I could not figure out the proper coding.
  elif userchoice == 'B':
      balance=printbalance()
      print('{:.2f}'.format(balance))
  elif userchoice == 'Q':
      print('Thank you for banking with us.\n')
      keep_going = False #here the loop ends with Q
      sys.exit()