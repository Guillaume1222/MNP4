import sqlite3
conn = sqlite3.connect('Annuaire.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS ANNUAIRE(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, nom TEXT, prenom TXT, numero INT, email TXT, qualite TXT)")


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
        numero=int(input("Numéro de téléphone: "))
        email=str(input("Email: "))
        qualite=str(input("Qualite: "))
        datas=(nom,prenom,numero,email,qualite)
        cur.execute("INSERT INTO ANNUAIRE(nom, prenom, numero, email, qualite) VALUES(?, ?, ?, ?, ?)",datas)
        conn.commit()

    if choix==2:#supprimer
        supprimer=str(input("nom à suprimer:",))
        suppr=(supprimer,)
        cur.execute('DELETE FROM annuaire WHERE nom = ?', suppr)
        conn.commit()

    if choix==3:#modifier
        print("1-modif_numéro")
        print("2-modif_email")
        chx=int(input("Quelle est votre choix: "))
        if chx==1 :
            nom=str(input("nom du contact: "))
            prenom=str(input("prenom du ocntact: "))
            numero=int(input("nouveau numéro: "))
            modifier1=(numero,nom,prenom)
            cur.execute('UPDATE annuaire SET numero = ? WHERE nom = ? AND prenom = ?', modifier1)
            conn.commit()
        else :
            nom=str(input("nom du contacte: "))
            prenom=str(input("prenom du contacte: "))
            email=str(input("nouveau email: "))
            modifier2=(email,nom,prenom)
            cur.execute('UPDATE annuaire SET email = ? WHERE nom = ? AND prenom = ?', modifier2)
            conn.commit()

    if choix==4:#rechercher
        cur.execute("select * from annuaire")
        print(cur.fetchall())

    if choix==5:#fin du programme
        menu=0
        print("Programme terminer")


conn.commit()
cur.close()
conn.close()