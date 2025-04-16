import random

def rps(you):
    game=["Taş","Kağıt","Makas"]
    robot=random.choice(game)
    print(f"Robotun seçimi:{robot}")
    if you==robot:
        print("Berabere")
    elif (you=="Taş" and robot=="Makas") or (you=="Kağıt" and robot=="Taş") or (you=="Makas" and robot=="Kağıt"):
        print("Kazandın!!!")
    else:
        print("Kaybettin!!!")


print("Taş Kağıt Makas oyununa hoşgeldinizz")
inn = input("Taş mı ,Kağıt mı ,Makas mı??: ").strip()
print(f"Senin seçimin:{inn}")
rps(inn)