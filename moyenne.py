
print("CE PROGRAMME TE PERMET DE SAVOIR QUEL EST TA MOYENNE TRIMESTRIELLE")
print()
print("Commenceons maintenant")
def calculer_moyenne_matiere(matiere:str,confission:int):
    devoir=input(f"Veuillez entrer la note du devoir de {matiere} ")
    while True:
        if not devoir.isdigit:
            print("Erreur!!Les notes de matieres sont uniquement coposer de chiffres")
            devoir=input(f"Veuillez entrer la note du devoir de {matiere} ")
        else:
            break
    evaluation=input(f"Veuillez entrer la note de l'evaluation de {matiere} ")
    while True:
        if not evaluation.isdigit:
            print("Erreur!!Les notes de matieres sont uniquement coposer de chiffres")
            evaluation=input(f"Veuillez entrer la note de l'evaluation de {matiere} ")
        else:
            break
    traveaux_pratiques=input(f"Veuillez entrer la note des traveaux pratiques de {matiere} ")
    while True:
        if not traveaux_pratiques.isdigit:
            print("Erreur!!Les notes de matieres sont uniquement coposer de chiffres")
            traveaux_pratiques=input(f"Veuillez entrer la note des traveaux pratiques de {matiere} ")
        else:
            break
    composition=input(f"Veuillez entrer la note de la composition de {matiere} ")
    while True:
        if not composition.isdigit:
            print("Erreur!!Les notes de matieres sont uniquement coposer de chiffres")
            composition=input(f"Veuillez entrer la note de la composition de {matiere} ")
        else:
            break
    moyenne_matiere=round((float(devoir)+float(evaluation)+float(traveaux_pratiques)+float(composition)*2)/5,2)
    return moyenne_matiere

mat=calculer_moyenne_matiere("math",5)
ph=calculer_moyenne_matiere("physique",4)
sc=calculer_moyenne_matiere("science",4)
ar=calculer_moyenne_matiere("arabe",3)
isl=calculer_moyenne_matiere("science islamique",2)
hg=calculer_moyenne_matiere("histoire-geo",2)
en=calculer_moyenne_matiere("anglais",2)
fr=calculer_moyenne_matiere("francais",2)
sp=calculer_moyenne_matiere("sport",1)
inf=calculer_moyenne_matiere("informatique",2)
tech=calculer_moyenne_matiere("technologie",2)
tm=calculer_moyenne_matiere("tamazight",2)
moyenne=(mat*5+ph*4+sc*4+ar*3+isl*2+hg*2+en*2+fr*2+sp*1+inf*2+tech*2+tm*2)/31



print("********************************************")
print("**      Matiere         **     Moyenne    **")
print("********************************************")
print(f"**      Math            **     {round(mat,2)}       **")
print(f"**      Physique        **     {round(ph,2)}       **")
print(f"**      Science         **     {round(sc,2)}       **")
print(f"**      Arabe           **     {round(ar,2)}       **")
print(f"**      Francais        **     {round(fr,2)}       **")
print(f"**      Anglais         **     {round(en,2)}       **")
print(f"**      Islamique       **     {round(isl,2)}       **")
print(f"**      Technologie     **     {round(tech,2)}       **")
print(f"**      Informatique    **     {round(inf,2)}       **")
print(f"**      Tamazight       **     {round(tm,2)}       **")
print(f"**      Sport           **     {round(sp,2)}       **")
print("********************************************")
print(f"** Moyenne generalle    **     {round(moyenne,2)}      **")
print("********************************************")