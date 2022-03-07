import random
print("Welcome to Rock Paper Scissors!")
score1 = score2 = 0
game = True
while game:
    move1 = input("\nEnter your move: (Rock(r),Paper(p),Scissors(s)): ")
    options = ["p","r","s"]
    move2 = random.choice(options)
    if move1=="p":
        if move2 == "r":
            score1 += 1
        elif move2 == "s":
            score2 += 1
        elif move2 == "p":
            pass
    elif move1=="r":
        if move2 == "s":
            score1 += 1
        elif move2 == "p":
            score2 += 1
        elif move2 == "r":
            pass    
    elif move1=="s":
        if move2 == "p":
            score1 += 1
        elif move2 == "r":
            score2 += 1
        elif move2 == "s":
            pass
    print("Player1: ",score1, "\tComputer: ",score2)    
    if score1 == 3:
        print("YOU WIN!")
        replay = input("Do you want to play again? (y) or (n)")
        if replay.lower() == "y":
            game = True
            score2 = score1 = 0
        else:
            game = False
    elif score2 == 3:
        print("YOU LOSE!")
        replay = input("Do you want to play again? (y) or (n): ")
        if replay.lower() == "y":
            game = True
            score2 = score1 = 0
        else:
            game = False
    else:
        continue


    
