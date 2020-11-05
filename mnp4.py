import sqlite3
conn = sqlite3.connect('Annuaire.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS ANNUAIRE(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, nom TEXT, prenom TXT, telephone INT, email TXT, qualite TXT)")


menu=int(1)
while menu!=0 :
    print("Base de données annuaire")
    print("1-Ajouter à la Base de donnée")
    print("2-Supprimer une entrée")
    print("3-Modifier Une entrée")
    print("4-Rechercher un élément")
    print("5-Quitter le menu")
    choix=int(input("Taper un chiffre entre 1 et 5: "))

    if choix==1:#ajouter
        nom=str(input("Nom:"))
        prenom=str(input("Prénom: "))
        telephone=int(input("Numéro de téléphone: "))
        email=str(input("Email: "))
        qualite=str(input("Qualite: "))
        datas=(nom,prenom,telephone,email,qualite)
        cur.execute("INSERT INTO ANNUAIRE(nom, prenom, telephone, email, qualite) VALUES(?, ?, ?, ?, ?)",datas)
        conn.commit()

    if choix==2:#supprimer
        supprimer=str(input("nom à suprimer:",))
        data_suppr=(supprimer,)
        cur.execute('DELETE FROM annuaire WHERE nom = ?', data_suppr)
        conn.commit()

    if choix==3:#modifier
        print("")
        print("1-modif_numéro")
        print("2-modif_email")
        print("3-modif_qualite")
        chx=int(input("Quelle est votre choix: "))
        if chx==1 :
            nom=str(input("nom du contact: "))
            prenom=str(input("prenom du ocntact: "))
            telephone=int(input("nouveau numéro: "))
            modifier1=(telephone,nom,prenom)
            cur.execute('UPDATE annuaire SET telephone = ? WHERE nom = ? AND prenom = ?', modifier1)
            conn.commit()
        elif chx==2 :
            nom=str(input("nom du contact: "))
            prenom=str(input("prenom du contact: "))
            email=str(input("nouveau email: "))
            modifier2=(email,nom,prenom)
            cur.execute('UPDATE annuaire SET email = ? WHERE nom = ? AND prenom = ?', modifier2)
            conn.commit()
        elif chx==3 :
            nom=str(input("nom du contact: "))
            prenom=str(input("prenom du contact: "))
            qualite=str(input("Nouveau type de qualite: "))
            modifier3=(qualite,nom,prenom)
            cur.execute('UPDATE annuaire SET qualite = ? WHERE nom = ? AND prenom = ?', modifier3)
            conn.commit()

    if choix==4:#rechercher
        champs=str(input("Insérer parmis les champs suivant selon la donnée que vous allez taper par la suite, merci de bien reproduire la syntaxe exacte donnée : nom , prenom , email , qualite : "))
        valeur=str(input("Rentrer ici la donnée que vous connaissez affilié au champ que vous avez rentré précédemment : "))

        cur.execute("select nom, prenom, telephone, email, qualite from annuaire where {}='{}'".format(champs, valeur))

        print(cur.fetchall())


    if choix==5:#fin du programme
        menu=0
        print("Programme terminer")


conn.commit()
cur.close()
conn.close()