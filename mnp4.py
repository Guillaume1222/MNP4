import sqlite3
conn = sqlite3.connect('Annuaire.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS annuaire(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, nom TEXT, prenom TXT,numéro INT, adresse_email TEXT, qualité TEXT)")


menu=int(1)
while menu!=0 :
    print("Base de données annuaire")
    print("1-Ajouter à la Base de donnée")
    print("2-Supprimer une entrée")
    print("3-Modifier Une entrée")
    print("4-Rechercher un élément")
    print("5-Quitter le menu")
    choix=int(input("Taper un chiffre entre 1 et 5:"))

    if choix==1:
        nom=str(input("Nom:"))
        prenom=str(input("Prénom:"))
        num=int(input("Numéro de téléphone:"))
        adresse_email=str(input("Email:"))
        qualite=str(input("Qualité:"))
        data=(nom,prenom,num,adresse_email,qualite)
        cur.execute("INSERT INTO annuaire(nom,prenom,numéro,adresse_email,qualite) VALUES(?, ?, ?, ?, ?)",data)
        conn.commit()

    if choix==2:
        supprime=input("nom à suprimer:",)
        suppr=(supprime,)
        cur.execute('DELETE FROM annuaire WHERE nom = ?', suppr)
        conn.commit()

    if choix==3:
        print("1-modif_numéro")
        print("2-modif_email")
        chx=int(input("Quelle est votre choix:"))
        if chx ==1 :
            numero=int(print("nouveau numéro:"))
            nom=str(print("nom du contact"))
            prenom=str(print("prenom du ocntact"))
            modif=(numero,nom,prenom)

    if choix==4:
        print("none")

    if choix==5:
        menu=0
        print("Programme terminer")


conn.commit()
cur.close()
conn.close()