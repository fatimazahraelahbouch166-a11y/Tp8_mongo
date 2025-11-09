from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client['EcommerceDB']
collection_client = db['Clients']
collection_product = db['Produits']
collection_commande = db['Commandes']
def CreateCommande():
    nom_client = input(" Entrer le nom du client : ")
    client_doc = collection_client.find_one({"Nom": nom_client})
    if not client_doc:
        print(" Client introuvable")
        return
    produits_commandes = []
    total = 0
    while True:
        nom_prod = input(" Entrer le nom du produit (ou 'stop' pour terminer) : ")
        if nom_prod.lower() == "stop":
            break
        produit = collection_product.find_one({"Nom": nom_prod})
        if produit:
            produits_commandes.append(produit['Nom'])
            total += produit['Prix']
        else:
            print("Produit introuvable")
 
    if not produits_commandes:
        print(" Aucun produit ajoute à la commande")
        return
    statut = input("Entrer le statut : ")
    Date_commande = input("Entrer la date de la commande : ")
    commande = {
        "Client": nom_client,
        "Produits": ", ".join(produits_commandes),
        "Date_commande": Date_commande,
        "Statut": statut,
        "Montant_total": total
    }
    collection_commande.insert_one(commande)
    print("Commande creee avec succes !")
    print("Details :")
    print(commande)
# CreateCommande()
# ________________________________Q2________________________________________
def AfficherAll_product():
    for prod in collection_product.find():
        print(prod)
#  AfficherAll_product()
# _________________________________Q3__________________________________________
def RechercherParClient():
    client=input("saisir le nom du client : ")
    for commande in collection_commande.find():
        if commande['Client']==client:
            print(commande)
# RechercherParClient()       
# ___________________________________Q4______________________________________________ 
def Commande_statut_liv():
    for commande in collection_commande.find():
        if commande['Statut']== "livrée":
            print(commande)
# Commande_statut_liv()
# _________________________________________Q5________________________________________________
def Update_product():
    Nom_prod=input("saisir le non du produit que vous pouvez modifier : ")
    produit = collection_product.find_one({"Nom": Nom_prod})
    if not produit :
        print("produit introuvable")
        exit()
    categorie=input("saisir la categorie: ")
    prix=float(input("saisir le nouveau prix : "))  
    stock=int(input("saisir le nombre disponible dans le stock : "))
    collection_product.update_one({"Nom":Nom_prod},{"$set":{"Catégorie": categorie,
            "Prix": prix,
            "Stock": stock}})
    print("produit bien modifier",collection_product.find_one({"Nom": Nom_prod}))
# Update_product()
# ___________________________________Q6______________________________________
def Ajouter_champ():
    collection_product.update_many({},{"$set":{"disponible":True}})
    print("champs disponible avec la valeur true par defaut est bien ajoute")
# Ajouter_champ()
# _________________________________________Q7_______________________________________
def RemoveCommandes(Client,Produit):
    commande=collection_commande.find_one({"Client":Client,"Produits":Produit})
    if not commande:
        print("commande introuvable")
        return 
    collection_commande.delete_one({"Client":Client,"Produits":Produit})
    print("commnande supprimer")
# RemoveCommandes("Fatima","2x Livre de recettes")
# ________________________________________________Q8_______________________________________
def RemoveCommandesParClient(Client):
    commande=collection_commande.find_one({"Client":Client})
    if not commande:
        print("commande introuvable")
        return 
    collection_commande.delete_one({"Client":Client})
    print("commnande bien supprimer")
# RemoveCommandesParClient("Hassan Al-Haddad")
# __________________________________________Q9_________________________________
def TrierCommande():
    All_commandes=collection_commande.find().sort({"Date_commande":-1})
    for commande in All_commandes:
        print(commande)
# TrierCommande()
# _____________________________________________Q10__________________________________________
def ShowProduct_dispo():
    Products=collection_product.find({"disponible":True})
    for prod in Products:
        print(prod)
# ShowProduct_dispo()    
def Menu():
    while True:
        print("_________________________MENU_______________________")
        print("1-Ajouter une commande ")
        print("2-Afficher tous les produits ")
        print("3-Afficher toute les commandes pour un client specifique ")
        print("4-Rechercher les commandes ayant le statut livree ")
        print("5-Mettre à jour un produit ")
        print("6-Ajouter nouveau champ ")
        print("7-Supprimer les commandes en fonction du produit et du client ")
        print("8-Supprimer les commandes d'un client donnee ")
        print("9-Trier les commandes par date de la commande ")
        print("10-Afficher les produits disponibles ")
        print("11-Quitter")
        choix=int(input("Choisir un nombre : "))
        if choix==1:
            CreateCommande()
        elif choix==2:
            AfficherAll_product()
        elif choix==3:
            RechercherParClient() 
        elif choix==4:
            Commande_statut_liv()
        elif choix==5:
            Update_product() 
        elif choix==6:
            Ajouter_champ()
        elif choix==7:
             RemoveCommandes("Fatima","2x Livre de recettes")
        elif choix==8:
            RemoveCommandesParClient("Hassan Al-Haddad")
        elif choix==9:
            TrierCommande()
        elif choix==10:
            ShowProduct_dispo()  
        elif choix==11:
            print("AU REVOIR")
            break
        else:
            print("choix invalid saisir un nombre entre 1 et 11")
            exit()
Menu()



