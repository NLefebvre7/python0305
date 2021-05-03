#from random import*
import random

fichier = open("dico.txt", "r")
liste_mots = fichier.readlines()    
mot = choice(liste_mots)            
mot = mot.rstrip()                
fichier.close()

mot_devine = "-" * len(mot)        
print(mot_devine)     

for i in range(5):
    while mot_devine!=mot:                                                                   
        lettre=input("Entrez une lettre : ")                                  
        for i in range(len(mot)):                                                        
            if lettre==mot[i]:                                                                     
        mot_devine = mot_devine[:i] + lettre + mot_devine[i+1:]                 
                                                                        
                                                                       
        print(mot_devine)
        if mot == mot_devine: 
        print ('Bravo ! Le mot',mot,'a été trouvé')
        break