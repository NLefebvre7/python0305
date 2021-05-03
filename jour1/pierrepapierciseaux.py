import random

leschoix = ["pierre","papier","ciseaux"]
ordi = random.choice(leschoix)
user = input("Choissis pierre, papier or ciseaux: ")
user = user.lower()




if user == 'pierre' or 'papier' or 'ciseaux':
    print ("Vous avez choisi", user , "l'ordi a choisi" , ordi)
if user == 'pierre':
    if ordi == 'pierre':
        print ('Match nul')
    elif ordi == 'papier':
        print ('Lordinateur a gagné')
    else:
        print ('Vous avez gagné')
if user == 'papier':
    if ordi == 'pierre':
        print ('Vous avez gagné')
    elif ordi == 'papier':
        print ('Match nul')
    else:
        print ('Lordinateur a gagné')
if user == 'ciseaux':
    if ordi == 'pierre':
        print ('Lordinateur a gagné')
    elif ordi == 'papier':
        print ('Vous avez gagné')
    else:
        print ('Match nul')