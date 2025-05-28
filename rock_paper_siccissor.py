import random

def rps(you):
    game=["Rock","Paper","Siccissor"]
    robot=random.choice(game)
    print(f"Robot's Choice:{robot}")
    if you==robot:
        print("DRAW")
    elif (you=="Rock" and robot=="Siccissor") or (you=="Paper" and robot=="Rock") or (you=="Siccissor" and robot=="Paper"):
        print("YOU WİN!!!")
    else:
        print("YOU LOSE!!!")


print("Welcome to Rock Paper Siccissor")
inn = input("Rock,Paper,Siccissor??: ").strip()
print(f"Your Choice:{inn}")
rps(inn)
