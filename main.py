import random

def game():
    print("You are playing a game")
    score=random.randint(1,1000)
    with open("higscore.txt") as f:
        highscore = f.read()
        if highscore !="":
            highscore=int(highscore)
        else:
            highscore=0
        print(f"Your score is {score}")
        if score>highscore:
            with open("higscore.txt","w") as f:
                f.write(str(score))
    return score

game()


