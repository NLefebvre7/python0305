import csv


leschoix = ["1","2","3","4","5"]
#user = user.lower()
choix1 = "Prise de commande"
choix2 = "Gestion des stock"
choix3 = "Gestion du menu"
choix4 = "Historique de commandes"
choix5 = "Quitter"

def display():
    chain = "\t\t      | Restaurant LIPSUM  |\n\t\t      |  15 rue des Ecoles |\n\t\t      |    08360 GIVET     |\n\t---------------\n\tMenu Principal:\n\t---------------\n 1. "+choix1+"\n 2. "+choix2+"\n 3. "+choix3+" \n 4. "+choix4+" \n 5. "+choix5+" \n\n "
    print(str(chain))


display()


user = input("Que voulez vous faire ? (1-5) \n")

# if user == '1' or '2' or '3' or '4' or '5':
#     print ("Vous avez choisi le choix numero", user,"")

if user == '2':
  print ("Affichage de la gestion des stocks :\n")

  f = open('stock.csv')
  csv_f = csv.reader(f)
  for row in csv_f:
      print("| ",row[0]," | ",row[1].ljust(15),"\t\t|",row[2])
  csvarray = []
  
  print ("\n\t Options :\n 1. Maj quantite\n 2. Ajouter produits\n 3. Supprimer produits\n 4. Exporter la liste \n 5. Retour au menu principal")
  user = input("Que voulez vous faire ? (1-4) \n")

  if user == '1':
    userchoix = input("De quel produits voulez vous modifier la quantité ? (Donnez l'ID du produit) \n")
    # for row in csv_f:
    #   print("| ",row[0]," | ",row[1].ljust(15),"\t\t|",row[2])
    # for row in csv_f:
    #   csvFileArray.append(row)
    #   print(csvFileArray[0])
    f = open('stock.csv')
    csv_f = csv.reader(f)
    one = int(userchoix)
    two = one + 1
    print ("Produit dont la quantité sera modifié :\n")
    for row in list(csv_f)[one:two]:
      print(row)
    userquantite = input("Nouvelle quantité ? \n")
    # row[2]=row[2].replace(userqauantite)
    for row in list(csv_f)[one:two]:

      print(row)



  if user == '2':
    userid = input("Quel ID a ce produit ? \n")
    usercnom = input("Quel nom a ce produit ? \n")
    userquantitee = input("Quel quantité de ce produit voulez vous ajouter ? \n")
    # f = open('stock.csv')
    # csv_f = csv.writer(f)
    # csv_f.writerow([userid,usercnom,userquantitee ])
  if user == '3':
    userchoix = input("Quel produit voulez vous supprimer ? (donnez l'ID) (irreversible) \n")
 #writer.writerow(row)
  if user == '4':
    print ("Export de la liste au format txt dans le repertoire courant..../\n")

  if user == '5':
    print ("Retour au menu principal :\n")
    display()