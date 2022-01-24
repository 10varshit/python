import random
name=input("whats your name: ")
words=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letter=random.choice(words)
print("Guess an alphabet")
guesses=''
turns=5
while turns>0:
    failed=0
    if failed==0:
        print("you guessed correctly, YOU WON")
        break
    guess=input("try again")

