import random
a=0
b=10
x=random.randint(a,b)
print(x)
n=int(input("enter a number"))
while(n==x):
    n=int(input("enter a number"))
    if n==x:
        print("YOUR ANS IS CORRECT "
              "try again")
        break

    elif n<x:
        print("TRY A NUMBER HIGHER")
        continue

    else:
        print("TRY A NUMBER LESSER")
        continue


