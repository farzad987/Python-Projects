import random
dice = [1,2,3,4,5,6]
while True:
    number = random.choice(dice)
    print(f"Your Number is : {number}")
    a=input("Do you want to play again? Yes or No ")
    if a=="No":
        break
