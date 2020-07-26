import random
print("Welcome to Guess The Number Between 1-100\n")
chosen=random.choice(list(range(0,101)))
counter=10
for i in range(0,10):
    player=int(input("Enter A Number: "))
    counter-=1
    difference = abs(chosen - player)
    if difference in list(range(50,101)):
        print("There is a BIG DIFFERENCE between the generated number\n")
        print(f"You have {counter} chances left")
    elif difference in list(range(10,50)):
        print("There is a SMALL DIFFERENCE between the generated number\n")
        print(f"You have {counter} chances left")
    elif difference in list(range(1,10)):
        print("There is a VERY SMALL DIFFERENCE between the generated number\n")
        print(f"You have {counter} chances left")
    if difference==0:
        print("Congratulations you have guessed the number")
        print(f"You have {counter} chances left")
        break
print(f"\nThe original number was {chosen}!!")

