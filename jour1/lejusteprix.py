import random

r=random.randint(0, 1000)
score = 20
print("Bienvenue dans le juste prix, un nombre aléatoire entre 0 et 1000 a ete generé, essayez de le trouver ! ")


while True:
    reponse = input()
    if int(reponse) == r:
        print("Vous avez gagné ! votre score est de : ", score, " points")
        break
    else:
        if int(reponse) > r:
            score = score - 1
            print("C'est moins que ", reponse)


        else:
            print("C'est plus que", reponse)
            score = score - 1