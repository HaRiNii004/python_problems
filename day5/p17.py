

a=input("enter the deposit amount: ").split(',')
b=input("enter the withdrawal amount: ").split(',')
Deposit=0
Withdrawal=0
for i in a:
      D=int(i)
      Deposit=Deposit+D

for j in b:
    W=int(j)
    Withdrawal=Withdrawal+W

amount=Deposit-Withdrawal
        
print (amount)