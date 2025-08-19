import os
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image , ImageTk
from tkinter import ttk
mn=tk.Tk()
mn.title('NoteMaster')
mn.geometry('768x614')
mn.resizable(False, False)
mn.iconbitmap(os.path.join(os.path.dirname(__file__), "download.ico"))
back = Image.open(os.path.join(os.path.dirname(__file__), "ecole.jpg"))
poto = ImageTk.PhotoImage(back)
mnbg = tk.Label(mn, image=poto)
mnbg.place(x=0, y=0, relheight=1, relwidth=1)
mat = Image.open(os.path.join(os.path.dirname(__file__), "mat.jpg"))
mat1 = mat.resize((26, 26), Image.Resampling.LANCZOS)
matf = ImageTk.PhotoImage(mat1)
mat_label = tk.Label(mn, image=matf)
ph = Image.open(os.path.join(os.path.dirname(__file__), "ph.jpg"))
ph1 = ph.resize((26, 26), Image.Resampling.LANCZOS)
phf = ImageTk.PhotoImage(ph1)
ph_label = tk.Label(mn, image=phf)
sc = Image.open(os.path.join(os.path.dirname(__file__), "sc.jpg"))
sc1 = sc.resize((26, 26), Image.Resampling.LANCZOS)
scf = ImageTk.PhotoImage(sc1)
sc_label = tk.Label(mn, image=scf)
ar = Image.open(os.path.join(os.path.dirname(__file__), "ar.png"))
ar1 = ar.resize((26, 26), Image.Resampling.LANCZOS)
arf = ImageTk.PhotoImage(ar1)
ar_label = tk.Label(mn, image=arf)
isl = Image.open(os.path.join(os.path.dirname(__file__), "is.jpg"))
isl1 = isl.resize((26, 26), Image.Resampling.LANCZOS)
islf = ImageTk.PhotoImage(isl1)
isl_label = tk.Label(mn, image=islf)
hg = Image.open(os.path.join(os.path.dirname(__file__), "hg.png"))
hg1 = hg.resize((26, 26), Image.Resampling.LANCZOS)
hgf = ImageTk.PhotoImage(hg1)
hg_label = tk.Label(mn, image=hgf)
en = Image.open(os.path.join(os.path.dirname(__file__), "en.jpg"))
en1 = en.resize((26, 26), Image.Resampling.LANCZOS)
enf = ImageTk.PhotoImage(en1)
en_label = tk.Label(mn, image=enf)
fr = Image.open(os.path.join(os.path.dirname(__file__), "fr.png"))
fr1 = fr.resize((26, 26), Image.Resampling.LANCZOS)
frf = ImageTk.PhotoImage(fr1)
fr_label = tk.Label(mn, image=frf)
sp = Image.open(os.path.join(os.path.dirname(__file__), "sp.jpg"))
sp1 = sp.resize((26, 26), Image.Resampling.LANCZOS)
spf = ImageTk.PhotoImage(sp1)
sp_label = tk.Label(mn, image=spf)
inf = Image.open(os.path.join(os.path.dirname(__file__), "inf.jpg"))
inf1 = inf.resize((26, 26), Image.Resampling.LANCZOS)
inff = ImageTk.PhotoImage(inf1)
inf_label = tk.Label(mn, image=inff)
tech = Image.open(os.path.join(os.path.dirname(__file__), "tech.jpg"))
tech1 = tech.resize((26, 26), Image.Resampling.LANCZOS)
techf = ImageTk.PhotoImage(tech1)
tech_label = tk.Label(mn, image=techf)
tm = Image.open(os.path.join(os.path.dirname(__file__), "tmz.png"))
tm1 = tm.resize((26, 26), Image.Resampling.LANCZOS)
tmf = ImageTk.PhotoImage(tm1)
tm_label = tk.Label(mn, image=tmf)
cv = Image.open(os.path.join(os.path.dirname(__file__), "civil.jpg"))
cv1=cv.resize((26,26), Image.Resampling.LANCZOS)
cvl=ImageTk.PhotoImage(cv1)
cvl_label=tk.Label(mn,image=cvl)
cvl_label.image = cvl
art = Image.open(os.path.join(os.path.dirname(__file__), "art.jpg"))
art1=art.resize((26,26), Image.Resampling.LANCZOS)
artl=ImageTk.PhotoImage(art1)
art_label=tk.Label(mn,image=artl)
art_label.image = artl
mu = Image.open(os.path.join(os.path.dirname(__file__), "mus.jpg"))
mus1=mu.resize((26,26), Image.Resampling.LANCZOS)
musl=ImageTk.PhotoImage(mus1)
mus_label=tk.Label(mn,image=musl)
mus_label.image = musl
ega = Image.open(os.path.join(os.path.dirname(__file__), "eg.png"))
ega1=ega.resize((26,26), Image.Resampling.LANCZOS)
egal=ImageTk.PhotoImage(ega1)
ega_label=tk.Label(mn,image=egal)
ega_label.image = egal
com = Image.open(os.path.join(os.path.dirname(__file__), "compt.jpg"))
com1=com.resize((26,26), Image.Resampling.LANCZOS)
coml=ImageTk.PhotoImage(com1)
com_label=tk.Label(mn,image=coml)
com_label.image = coml
filo = Image.open(os.path.join(os.path.dirname(__file__), "filo.png"))
filo1=filo.resize((26,26), Image.Resampling.LANCZOS)
filol=ImageTk.PhotoImage(filo1)
filo_label=tk.Label(mn,image=filol)
filo_label.image = filol
lang3 = Image.open(os.path.join(os.path.dirname(__file__), "langue3.png"))
lang31=lang3.resize((26,26), Image.Resampling.LANCZOS)
lang3l=ImageTk.PhotoImage(lang31)
lang3_label=tk.Label(mn,image=lang3l)
lang3_label.image = lang3l
settings = Image.open(os.path.join(os.path.dirname(__file__), "setting1.jpg"))
settings = settings.resize((50, 50), Image.Resampling.LANCZOS)
sfl = ImageTk.PhotoImage(settings)
settingsbg=Image.open(os.path.join(os.path.dirname(__file__),"par.jpg"))
settingsbg=settingsbg.resize((400,265), Image.Resampling.LANCZOS)
bgsetf=ImageTk.PhotoImage(settingsbg)
close=Image.open(os.path.join(os.path.dirname(__file__),"close.jpg"))
close=close.resize((50,50), Image.Resampling.LANCZOS)
closebt=ImageTk.PhotoImage(close)
mn.update()
moyennes_globales=[]
coefissions=[]
cofpos=[0,1,2,3,4,5,6,7]
cofposprim=[0,1]
niveau="1 AS"
nivpos=["1 AP","2 AP","3 AP","4 AP","5 AP","1 AM","2 AM","3 AM","4 AM","1 AS","1 AL","2 Math","2 Science","2 Math-tech","2 Lettres-Philo","2 EG","2 Langues","3 Math","3 Science","3 Lettres-Philo","3 EG","3 Langues","3 Math-tech"]
remarq=tk.Label(mn,text="Veuillez accéder au paramètres de l'aplication\npour choisir votre niveau scolaire",font=("Arial",28),bg="#06659c",fg="white")
remarq.place(x=11,y=300)
remarque=tk.Label(mn,text="Remarque:\nPour réutiliser cette application avec un autre niveau scolaire\nvous devez la redémarer",font=("Arial",21),bg="red",fg="white")
remarque.place(x=7,y=100)
cal = Image.open(os.path.join(os.path.dirname(__file__), "cal.png"))
cal1 = cal.resize((40, 53), Image.Resampling.LANCZOS)
calf = ImageTk.PhotoImage(cal1)
calculer = tk.Label(mn, image=calf)
def calculer_moyenne_matiere(matiere:str,confition:int,xx,yy):
    if matiere=="Math":
        mat_label.place(x=385, y=yy-3)
    elif matiere=="Physique":
        ph_label.place(x=385, y=yy-3)
    elif matiere=="Science"or matiere=="S-Techno":
        sc_label.place(x=385, y=yy-3)
    elif matiere=="Histoire-Geo":
        hg_label.place(x=385, y=yy-3)
    elif matiere=="S-Islamique" or matiere=="E-Islamique":
        isl_label.place(x=385, y=yy-3)
    elif matiere=="Arabe":
        ar_label.place(x=385, y=yy-3)
    elif matiere=="Anglais":
        en_label.place(x=385, y=yy-3)
    elif matiere=="Français":
        fr_label.place(x=385, y=yy-3)
    elif matiere=="Technologie":
        tech_label.place(x=385, y=yy-3)
    elif matiere=="Informatique":
        inf_label.place(x=385, y=yy-3)
    elif matiere=="Tamazight":
        tm_label.place(x=385, y=yy-3)
    elif matiere=="Sport":
        sp_label.place(x=385,y=yy-3)
    elif matiere=="E-civil" or matiere=="Droit":
        cvl_label.place(x=385, y=yy-3)
    elif matiere=="Art":
        art_label.place(x=385, y=yy-3)
    elif matiere=="Musique":
        mus_label.place(x=385, y=yy-3)
    elif matiere=="EG":
        ega_label.place(x=385,y=yy-3)
    elif matiere=="Comptabilité":
        com_label.place(x=385,y=yy-3)
    elif matiere=="Philosophie":
        filo_label.place(x=385,y=yy-3)
    elif matiere=="Langue 3":
        lang3_label.place(x=385,y=yy-3)
    calculer.place(x=xx+100, y=550)
    global moyennes_globales,coefissions
    sub=tk.Label(mn,text=matiere,font=("Arial",10),bg="green",fg="white")
    dm=tk.Label(mn,text="Devoir",font=("Arial",10),bg="red",fg="white")
    em=tk.Label(mn,text="Evaluation",font=("Arial",10),bg="red",fg="white")
    tm=tk.Label(mn,text="TP",font=("Arial",10),bg="red",fg="white")
    co=tk.Label(mn,text="Composition",font=("Arial",10),bg="red",fg="white")
    coe=tk.Label(mn,text="Coeffitient",font=("ARIAL",10),bg="red",fg="white")
    sub.place(x=17,y=yy)
    dm.place(x=xx,y=3)
    em.place(x=xx+50,y=3)
    tm.place(x=xx+120,y=3)
    co.place(x=xx+150,y=3)
    coe.place(x=xx+250,y=3)
    d=tk.Entry(mn,bg="grey",fg="white",width=5,font=("Arial",14))
    d.place(x=xx,y=yy)
    e=tk.Entry(mn,bg="grey",fg="white",width=5,font=("Arial",14))
    e.place(x=(xx+62),y=yy)
    t=tk.Entry(mn,bg="grey",fg="white",width=5,font=("Arial",14))
    t.place(x=(xx+124),y=yy)
    c=tk.Entry(mn,bg="grey",fg="white",width=5,font=("Arial",14))
    c.place(x=(xx+186),y=yy)
    cofer=tk.Label(mn,text="",font=("Arial"),bg="red",fg="white")
    cofer.place(x=xx+475,y=yy)
    cofer.place_forget()
    conf=ttk.Combobox(mn,values=cofpos,state="readonly",font=("Arial"),width=1,cursor="hand2")
    conf.place(x=xx+250,y=yy)
    conf.set(confition)
    er = tk.Label(mn, text=f"Erreur!!Veuillez rentrer les notes de {matiere} entre 0 et 20", bg="red", fg="white") 
    er.place(x=xx,y=yy+25)
    er.place_forget()
    def moyennedematiere():
        try:
            if 0<=float(d.get())<=20 and 0<=float(e.get())<=20 and 0<=float(t.get())<=20 and 0<=float(c.get())<=20:
                devoir=float(d.get())
                evaluation=float(e.get())
                traveaux_pratiques=float(t.get())
                composition=float(c.get())
                moyenne_matiere=round((float(devoir)+float(evaluation)+float(traveaux_pratiques)+(float(composition)*2))/5,2) 
                moyennes_globales.append(moyenne_matiere)
                confvoulu=int(conf.get())
                coefissions.append(confvoulu)
                er.place_forget()
                press.place_forget()
                if moyenne_matiere<10:
                    ms=tk.Label(mn,text=f"Moyenne {matiere}={moyenne_matiere} / 20",font=("Arial",15),bg="red",fg="white")
                    ms.place(x=xx+325,y=yy)
                elif 10<=moyenne_matiere<=16.99:
                    ms=tk.Label(mn,text=f"Moyenne {matiere}={moyenne_matiere} / 20",font=("Arial",15),bg="orange",fg="white")
                    ms.place(x=xx+325,y=yy)
                elif 17<=moyenne_matiere<=17.99: 
                    ms=tk.Label(mn,text=f"Moyenne {matiere}={moyenne_matiere} / 20",font=("Arial",15),bg="blue",fg="white")
                    ms.place(x=xx+325,y=yy)
                elif moyenne_matiere>=18:
                    ms=tk.Label(mn,text=f"Moyenne {matiere}={moyenne_matiere} / 20",font=("Arial",15), bg="green",fg="white")
                    ms.place(x=xx+325,y=yy)
            else:
                er.config(text=f"Erreur!!Veuillez rentrer les notes de {matiere} entre 0 et 20",bg="red",fg="white")
                er.place(x=xx,y=yy+25)
        except ValueError:
            er.place(x=xx,y=yy+25)
    press=tk.Button(mn,text=f"Calculer moyenne {matiere}",command=lambda:moyennedematiere(),bg="blue",fg="white",width=24,cursor="hand2")
    press.place(x=xx+325,y=yy)
    return
def calculer_moyenne_matierep(matiere:str,confition:int,xx,yy):
    if matiere=="Math":
        mat_label.place(x=385, y=yy-3)
    elif matiere=="S-Technologie":
        sc_label.place(x=385, y=yy-3)
    elif matiere=="Histoire-Geo":
        hg_label.place(x=385, y=yy-3)
    elif matiere=="E-Islamique":
        isl_label.place(x=385, y=yy-3)
    elif matiere=="Arabe":
        ar_label.place(x=385, y=yy-3)
    elif matiere=="Anglais":
        en_label.place(x=385, y=yy-3)
    elif matiere=="Français":
        fr_label.place(x=385, y=yy-3)
    elif matiere=="Tamazight":
        tm_label.place(x=385, y=yy-3)
    elif matiere=="Sport":
        sp_label.place(x=385,y=yy-3)
    elif matiere=="E-civil":
        cvl_label.place(x=385, y=yy-3)
    elif matiere=="Art":
        art_label.place(x=385, y=yy-3)
    elif matiere=="Musique":
        mus_label.place(x=385, y=yy-3)
    calculer.place(x=xx+100, y=550)
    global moyennes_globales,coefissions
    sub=tk.Label(mn,text=matiere,font=("Arial",10),bg="green",fg="white")
    em=tk.Label(mn,text="Evaluation",font=("Arial",10),bg="red",fg="white")
    co=tk.Label(mn,text="Composition",font=("Arial",10),bg="red",fg="white")
    coe=tk.Label(mn,text="Coeffitient",font=("ARIAL",10),bg="red",fg="white")
    sub.place(x=50,y=yy)
    em.place(x=xx+50,y=3)
    co.place(x=xx+150,y=3)
    coe.place(x=xx+250,y=3)
    e=tk.Entry(mn,bg="grey",fg="white",width=5,font=("Arial",14))
    e.place(x=xx+55,y=yy)
    c=tk.Entry(mn,bg="grey",fg="white",width=5,font=("Arial",14))
    c.place(x=(xx+155),y=yy)
    cofer=tk.Label(mn,text="",font=("Arial"),bg="red",fg="white")
    cofer.place(x=xx+475,y=yy)
    cofer.place_forget()
    conf=ttk.Combobox(mn,values=cofposprim,state="readonly",font=("Arial"),width=1,cursor="hand2")
    conf.place(x=xx+250,y=yy)
    conf.set(confition)
    er = tk.Label(mn, text=f"Erreur!!Veuillez rentrer les notes de {matiere} entre 0 et 10", bg="red", fg="white") 
    er.place(x=xx,y=yy+25)
    er.place_forget()
    def moyennedematiere():
        try:
            if 0<=float(e.get())<=10 and 0<=float(c.get())<=10:
                evaluation=float(e.get())
                composition=float(c.get())
                moyenne_matiere=round((float(evaluation)+float(composition))/2,2) 
                moyennes_globales.append(moyenne_matiere)
                confvoulu=int(conf.get())
                coefissions.append(confvoulu)
                er.place_forget()
                press.place_forget()
                if moyenne_matiere<5:
                    ms=tk.Label(mn,text=f"Moyenne {matiere}={moyenne_matiere} / 10",font=("Arial",15),bg="red",fg="white")
                    ms.place(x=xx+325,y=yy)
                elif 5<=moyenne_matiere<=7.99:
                    ms=tk.Label(mn,text=f"Moyenne {matiere}={moyenne_matiere} / 10",font=("Arial",15),bg="orange",fg="white")
                    ms.place(x=xx+325,y=yy)
                elif 8<=moyenne_matiere<=8.99: 
                    ms=tk.Label(mn,text=f"Moyenne {matiere}={moyenne_matiere} / 10",font=("Arial",15),bg="blue",fg="white")
                    ms.place(x=xx+325,y=yy)
                elif moyenne_matiere>=9:
                    ms=tk.Label(mn,text=f"Moyenne {matiere}={moyenne_matiere} / 10",font=("Arial",15), bg="green",fg="white")
                    ms.place(x=xx+325,y=yy)
            else:
                er.config(text=f"Erreur!!Veuillez rentrer les notes de {matiere} entre 0 et 10",bg="red",fg="white")
                er.place(x=xx,y=yy+25)
        except ValueError:
            er.place(x=xx,y=yy+25)
    press=tk.Button(mn,text=f"Calculer moyenne {matiere}",command=lambda:moyennedematiere(),bg="blue",fg="white",width=24,cursor="hand2")
    press.place(x=xx+325,y=yy)
    return
def parametres():
    global niveau,remarq,remarque,coefissions
    par=tk.Label(mn,image=bgsetf)
    par.place(x=359,y=8)
    nivlab=tk.Label(mn,text="Niveau scolaire :",font=("Arial",20),bg="#1c9be6")
    nivlab.place(x=370,y=60)
    nivea=ttk.Combobox(mn,values=nivpos,state="readonly",font=("Arial",20),cursor="hand2")
    nivea.place(x=405,y=125)
    nivea.set(niveau)
    def conf():
        global remarque,remarq,niveau,coefissions
        remarq.place_forget()
        remarque.place_forget()
        par.place_forget()
        nivea.place_forget()
        nivlab.place_forget()
        confe.place_forget()
        closebtf.place_forget()
        setb.place_forget()
        niveau=nivea.get()
        salut=tk.Label(mn,text=f"Compteur moyenne {niveau}",font=("Arial",0,"bold"))
        salut.place(x=430,y=3)
        def calculermoyenne():
            global moyennes_globales,coefissions
            if niveau == "4 AP" or niveau == "5 AP" or niveau == "3 AP" or niveau == "2 AP" or niveau == "1 AP":
                if len(coefissions) == 10 and len(moyennes_globales) == 10:  
                    moyenne = (moyennes_globales[0] * coefissions[0] + moyennes_globales[1] * coefissions[1] + moyennes_globales[2] * coefissions[2] + moyennes_globales[3] * coefissions[3] + moyennes_globales[4] * coefissions[4] + moyennes_globales[5] * coefissions[5] + moyennes_globales[6] * coefissions[6] + moyennes_globales[7] * coefissions[7] + moyennes_globales[8] * coefissions[8] + moyennes_globales[9] * coefissions[9]) / (coefissions[0] + coefissions[1] + coefissions[2] + coefissions[3] + coefissions[4] + coefissions[5] + coefissions[6] + coefissions[7] + coefissions[8] + coefissions[9])
                    moyenne = round(moyenne, 2)
                    moyerrer.place_forget()
                    if moyenne < 5:
                        ms = tk.Label(mn, text=f"Oups, votre moyenne est : {moyenne} / 10", font=("Arial", 15), bg="red", fg="white")
                        ms.place(x=250, y=565)
                    elif 5 <= moyenne <= 7.99:
                        ms = tk.Label(mn, text=f"C'était presque, votre moyenne est : {moyenne} / 10", font=("Arial", 15), bg="orange", fg="white")
                        ms.place(x=250, y=565)
                    elif 8 <= moyenne <= 9:
                        ms = tk.Label(mn, text=f"Félicitation! Votre moyenne est : {moyenne} / 10", font=("Arial", 15), bg="blue", fg="white")
                        ms.place(x=250, y=565)
                    elif moyenne >= 9:
                        ms = tk.Label(mn, text=f"Félicitation! Votre moyenne est : {moyenne} / 10", font=("Arial", 15), bg="green", fg="white")
                        ms.place(x=250, y=565)
                    moyennes_globales = []
                    coefissions = []
                    moy.place_forget()
                else:
                    moyerrer.config(text="Erreur! Calculez d'abord les moyennes des matières!\nSi vous n'étudiez pas une matière,\nmettez coefficient=0 avec des notes de votre choix")
                    moyerrer.place(x=250, y=545)
            elif niveau == "1 AS" or niveau == "1 AM" or niveau == "2 AM" or niveau == "3 AM" or niveau == "4 AM":
                if len(coefissions) == 12 and len(moyennes_globales) == 12:  
                    moyenne = (moyennes_globales[0] * coefissions[0] + moyennes_globales[1] * coefissions[1] + moyennes_globales[2] * coefissions[2] + moyennes_globales[3] * coefissions[3] + moyennes_globales[4] * coefissions[4] + moyennes_globales[5] * coefissions[5] + moyennes_globales[6] * coefissions[6] + moyennes_globales[7] * coefissions[7] + moyennes_globales[8] * coefissions[8] + moyennes_globales[9] * coefissions[9] + moyennes_globales[10] * coefissions[10] + moyennes_globales[11] * coefissions[11]) / (coefissions[0] + coefissions[1] + coefissions[2] + coefissions[3] + coefissions[4] + coefissions[5] + coefissions[6] + coefissions[7] + coefissions[8] + coefissions[9] + coefissions[10] + coefissions[11])
                    moyenne = round(moyenne, 2)
                    moyerrer.place_forget()
                    if moyenne < 10:
                        ms = tk.Label(mn, text=f"Oups, votre moyenne est : {moyenne} / 20", font=("Arial", 15), bg="red", fg="white")
                        ms.place(x=250, y=565)
                    elif 10 <= moyenne <= 16.99:
                        ms = tk.Label(mn, text=f"C'était presque, votre moyenne est : {moyenne} / 20", font=("Arial", 15), bg="orange", fg="white")
                        ms.place(x=250, y=565)
                    elif 17 <= moyenne <= 17.99:
                        ms = tk.Label(mn, text=f"Félicitation! Votre moyenne est : {moyenne} / 20", font=("Arial", 15), bg="blue", fg="white")
                        ms.place(x=250, y=565)
                    elif moyenne >= 18:
                        ms = tk.Label(mn, text=f"Félicitation! Votre moyenne est : {moyenne} / 20", font=("Arial", 15), bg="green", fg="white")
                        ms.place(x=250, y=565)
                    moyennes_globales = []
                    coefissions = []
                    moy.place_forget()
                else:
                    moyerrer.config(text="Erreur! Calculez d'abord les moyennes des matières!\nSi vous n'étudiez pas une matière,\nmettez coefficient=0 avec des notes de votre choix")
                    moyerrer.place(x=250, y=545)
            elif niveau== "1 AL" or niveau == "2 Science" or niveau == "2 Math" or niveau == "2 Math-tech" or niveau == "2 EG" or niveau == "2 Langues" or niveau == "2 Létres-Philo":
                if len(coefissions) == 11 and len(moyennes_globales) == 11:  
                    moyenne = (moyennes_globales[0] * coefissions[0] + moyennes_globales[1] * coefissions[1] + moyennes_globales[2] * coefissions[2] + moyennes_globales[3] * coefissions[3] + moyennes_globales[4] * coefissions[4] + moyennes_globales[5] * coefissions[5] + moyennes_globales[6] * coefissions[6] + moyennes_globales[7] * coefissions[7] + moyennes_globales[8] * coefissions[8] + moyennes_globales[9] * coefissions[9] + moyennes_globales[10] * coefissions[10]) / (coefissions[0] + coefissions[1] + coefissions[2] + coefissions[3] + coefissions[4] + coefissions[5] + coefissions[6] + coefissions[7] + coefissions[8] + coefissions[9] + coefissions[10])
                    moyenne = round(moyenne, 2)
                    moyerrer.place_forget()
                    if moyenne < 10:
                        ms = tk.Label(mn, text=f"Oups, votre moyenne est : {moyenne} / 20", font=("Arial", 15), bg="red", fg="white")
                        ms.place(x=250, y=565)
                    elif 10 <= moyenne <= 16.99:
                        ms = tk.Label(mn, text=f"C'était presque, votre moyenne est : {moyenne} / 20", font=("Arial", 15), bg="orange", fg="white")
                        ms.place(x=250, y=565)
                    elif 17 <= moyenne <= 17.99:
                        ms = tk.Label(mn, text=f"Félicitation! Votre moyenne est : {moyenne} / 20", font=("Arial", 15), bg="blue", fg="white")
                        ms.place(x=250, y=565)
                    elif moyenne >= 18:
                        ms = tk.Label(mn, text=f"Félicitation! Votre moyenne est : {moyenne} / 20", font=("Arial", 15), bg="green", fg="white")
                        ms.place(x=250, y=565)
                    moyennes_globales = []
                    coefissions = []
                    moy.place_forget()
                else:
                    moyerrer.config(text="Erreur! Calculez d'abord les moyennes des matières!\nSi vous n'étudiez pas une matière,\nmettez coefficient=0 avec des notes de votre choix")
                    moyerrer.place(x=250, y=545)
            elif niveau == "3 EG" or niveau == "3 Science" or niveau == "3 Math-tech" or niveau == "3 Math" or niveau == "3 Langues" or niveau == "3 Létres-Philo":
                if len(coefissions) == 11 and len(moyennes_globales) == 11:  
                    moyenne = (moyennes_globales[0] * coefissions[0] + moyennes_globales[1] * coefissions[1] + moyennes_globales[2] * coefissions[2] + moyennes_globales[3] * coefissions[3] + moyennes_globales[4] * coefissions[4] + moyennes_globales[5] * coefissions[5] + moyennes_globales[6] * coefissions[6] + moyennes_globales[7] * coefissions[7] + moyennes_globales[8] * coefissions[8] + moyennes_globales[9] * coefissions[9] + moyennes_globales[10] * coefissions[10]) / (coefissions[0] + coefissions[1] + coefissions[2] + coefissions[3] + coefissions[4] + coefissions[5] + coefissions[6] + coefissions[7] + coefissions[8] + coefissions[9] + coefissions[10])
                    moyenne = round(moyenne, 2)
                    moyerrer.place_forget()
                    if moyenne < 10:
                        ms = tk.Label(mn, text=f"Oups, votre moyenne est : {moyenne} / 20", font=("Arial", 15), bg="red", fg="white")
                        ms.place(x=250, y=565)
                    elif 10 <= moyenne <= 16.99:
                        ms = tk.Label(mn, text=f"C'était presque, votre moyenne est : {moyenne} / 20", font=("Arial", 15), bg="orange", fg="white")
                        ms.place(x=250, y=565)
                    elif 17 <= moyenne <= 17.99:
                        ms = tk.Label(mn, text=f"Félicitation! Votre moyenne est : {moyenne} / 20", font=("Arial", 15), bg="blue", fg="white")
                        ms.place(x=250, y=565)
                    elif moyenne >= 18:
                        ms = tk.Label(mn, text=f"Félicitation! Votre moyenne est : {moyenne} / 20", font=("Arial", 15), bg="green", fg="white")
                        ms.place(x=250, y=565)
                    moyennes_globales = []
                    coefissions = []
                    moy.place_forget()
                else:
                    moyerrer.config(text="Erreur! Comptez d'abord les moyennes des matières!\nSi vous n'étudiez pas une matière,\nmettez coefficient=0 avec des notes de votre choix")
                    moyerrer.place(x=250, y=545)
        if niveau=="1 AS":
            mat=calculer_moyenne_matiere("Math",5,100,35)
            ph=calculer_moyenne_matiere("Physique",4,100,78)
            sc=calculer_moyenne_matiere("Science",4,100,121)
            ar=calculer_moyenne_matiere("Arabe",3,100,164)
            isl=calculer_moyenne_matiere("S-Islamique",2,100,207)
            hg=calculer_moyenne_matiere("Histoire-Geo",2,100,250)
            en=calculer_moyenne_matiere("Anglais",2,100,293)
            fr=calculer_moyenne_matiere("Français",2,100,336)
            sp=calculer_moyenne_matiere("Sport",1,100,379)
            inf=calculer_moyenne_matiere("Informatique",2,100,422)
            tech=calculer_moyenne_matiere("Technologie",2,100,465)
            tm=calculer_moyenne_matiere("Tamazight",2,100,508)
        elif niveau=="1 AM" :
            mat=calculer_moyenne_matiere("Math",2,100,35)
            ph=calculer_moyenne_matiere("Physique",1,100,78)
            sc=calculer_moyenne_matiere("Science",1,100,121)
            ar=calculer_moyenne_matiere("Arabe",2,100,164)
            isl=calculer_moyenne_matiere("E-Islamique",1,100,207)
            hg=calculer_moyenne_matiere("Histoire-Geo",2,100,250)
            en=calculer_moyenne_matiere("Anglais",1,100,293)
            fr=calculer_moyenne_matiere("Français",1,100,336)
            sp=calculer_moyenne_matiere("Sport",1,100,379)
            inf=calculer_moyenne_matiere("Informatique",1,100,422)
            cvl=calculer_moyenne_matiere("E-civil",1,100,465)
            tm=calculer_moyenne_matiere("Tamazight",2,100,508)
        elif niveau=="2 AM" or niveau=="3 AM" :
            mat=calculer_moyenne_matiere("Math",3,100,35)
            ph=calculer_moyenne_matiere("Physique",2,100,78)
            sc=calculer_moyenne_matiere("Science",2,100,121)
            ar=calculer_moyenne_matiere("Arabe",3,100,164)
            isl=calculer_moyenne_matiere("E-Islamique",1,100,207)
            hg=calculer_moyenne_matiere("Histoire-Geo",2,100,250)
            en=calculer_moyenne_matiere("Anglais",1,100,293)
            fr=calculer_moyenne_matiere("Français",1,100,336)
            sp=calculer_moyenne_matiere("Sport",1,100,379)
            inf=calculer_moyenne_matiere("Informatique",1,100,422)
            cvl=calculer_moyenne_matiere("E-civil",1,100,465)
            tm=calculer_moyenne_matiere("Tamazight",2,100,508)
        elif niveau=="4 AM":
            mat=calculer_moyenne_matiere("Math",4,100,35)
            ph=calculer_moyenne_matiere("Physique",2,100,78)
            sc=calculer_moyenne_matiere("Science",2,100,121)
            ar=calculer_moyenne_matiere("Arabe",5,100,164)
            isl=calculer_moyenne_matiere("E-Islamique",2,100,207)
            hg=calculer_moyenne_matiere("Histoire-Geo",3,100,250)
            en=calculer_moyenne_matiere("Anglais",2,100,293)
            fr=calculer_moyenne_matiere("Français",3,100,336)
            sp=calculer_moyenne_matiere("Sport",1,100,379)
            inf=calculer_moyenne_matiere("Informatique",1,100,422)
            cvl=calculer_moyenne_matiere("E-civil",1,100,465)
            tm=calculer_moyenne_matiere("Tamazight",2,100,508)
        elif niveau=="1 AL":
            ar=calculer_moyenne_matiere("Arabe",5,100,35)
            isl=calculer_moyenne_matiere("S-Islamique",2,100,78)
            hg=calculer_moyenne_matiere("Histoire-Geo",3,100,121)
            ph=calculer_moyenne_matiere("Art",1,100,164)
            fr=calculer_moyenne_matiere("Français",3,100,207)
            en=calculer_moyenne_matiere("Anglais",3,100,250)
            sp=calculer_moyenne_matiere("Sport",1,100,293)
            inf=calculer_moyenne_matiere("Informatique",2,100,336)
            tm=calculer_moyenne_matiere("Tamazight",2,100,379)
            ph=calculer_moyenne_matiere("Physique",2,100,422)
            sc=calculer_moyenne_matiere("Science",2,100,465)
        elif niveau=="4 AP" or niveau=="5 AP"or niveau=="3 AP"or niveau=="2 AP"or niveau=="1 AP":
            ar=calculer_moyenne_matierep("Math",1,100,35)
            isl=calculer_moyenne_matierep("E-Islamique",1,100,78)
            hg=calculer_moyenne_matierep("Histoire-Geo",1,100,121)
            ph=calculer_moyenne_matierep("Art",1,100,164)
            fr=calculer_moyenne_matierep("Français",1,100,207)
            en=calculer_moyenne_matierep("Anglais",1,100,250)
            sp=calculer_moyenne_matierep("Sport",1,100,293)
            inf=calculer_moyenne_matierep("Musique",1,100,336)
            tm=calculer_moyenne_matierep("Tamazight",1,100,379)
            ph=calculer_moyenne_matierep("S-Technologie",1,100,422)
            sc=calculer_moyenne_matierep("Arabe",2,100,465)
            tech=calculer_moyenne_matierep("E-civil",1,100,508)
        elif niveau=="2 Science":
            mat=calculer_moyenne_matiere("Math",5,100,35)
            ph=calculer_moyenne_matiere("Physique",5,100,78)
            sc=calculer_moyenne_matiere("Science",6,100,121)
            ar=calculer_moyenne_matiere("Arabe",2,100,164)
            isl=calculer_moyenne_matiere("S-Islamique",2,100,207)
            hg=calculer_moyenne_matiere("Histoire-Geo",2,100,250)
            en=calculer_moyenne_matiere("Anglais",2,100,293)
            fr=calculer_moyenne_matiere("Français",2,100,336)
            sp=calculer_moyenne_matiere("Sport",1,100,379)
            inf=calculer_moyenne_matiere("Tamazight",2,100,422)
            tech=calculer_moyenne_matiere("Art",1,100,465)
        elif niveau=="2 Math":
            mat=calculer_moyenne_matiere("Math",7,100,35)
            ph=calculer_moyenne_matiere("Physique",6,100,78)
            sc=calculer_moyenne_matiere("Science",2,100,121)
            ar=calculer_moyenne_matiere("Arabe",2,100,164)
            isl=calculer_moyenne_matiere("S-Islamique",2,100,207)
            hg=calculer_moyenne_matiere("Histoire-Geo",2,100,250)
            en=calculer_moyenne_matiere("Anglais",2,100,293)
            fr=calculer_moyenne_matiere("Français",2,100,336)
            sp=calculer_moyenne_matiere("Sport",1,100,379)
            inf=calculer_moyenne_matiere("Tamazight",2,100,422)
            tech=calculer_moyenne_matiere("Art",1,100,465)
        elif niveau=="2 Math-tech":
            mat=calculer_moyenne_matiere("Math",6,100,35)
            ph=calculer_moyenne_matiere("Physique",5,100,78)
            sc=calculer_moyenne_matiere("Technologie",6,100,121)
            ar=calculer_moyenne_matiere("Arabe",2,100,164)
            isl=calculer_moyenne_matiere("S-Islamique",2,100,207)
            hg=calculer_moyenne_matiere("Histoire-Geo",2,100,250)
            en=calculer_moyenne_matiere("Anglais",2,100,293)
            fr=calculer_moyenne_matiere("Français",2,100,336)
            sp=calculer_moyenne_matiere("Sport",1,100,379)
            inf=calculer_moyenne_matiere("Tamazight",2,100,422)
            tech=calculer_moyenne_matiere("Art",1,100,465)
        elif niveau=="2 EG":
            mat=calculer_moyenne_matiere("Math",3,100,35)
            ph=calculer_moyenne_matiere("Comptabilité",5,100,78)
            sc=calculer_moyenne_matiere("EG",4,100,121)
            ar=calculer_moyenne_matiere("Droit",2,100,164)
            isl=calculer_moyenne_matiere("S-Islamique",2,100,207)
            hg=calculer_moyenne_matiere("Histoire-Geo",3,100,250)
            en=calculer_moyenne_matiere("Anglais",2,100,293)
            fr=calculer_moyenne_matiere("Français",2,100,336)
            sp=calculer_moyenne_matiere("Sport",1,100,379)
            inf=calculer_moyenne_matiere("Tamazight",2,100,422)
            cvl=calculer_moyenne_matiere("Arabe",2,100,465)
            tech=calculer_moyenne_matiere("Art",1,100,508)
        elif niveau=="2 Langues":
            mat=calculer_moyenne_matiere("Math",2,100,35)
            ph=calculer_moyenne_matiere("Arabe",4,100,78)
            sc=calculer_moyenne_matiere("Anglais",4,100,121)
            ar=calculer_moyenne_matiere("Langue 3",4,100,164)
            isl=calculer_moyenne_matiere("S-Islamique",2,100,207)
            hg=calculer_moyenne_matiere("Histoire-Geo",4,100,250)
            en=calculer_moyenne_matiere("Français",4,100,293)
            fr=calculer_moyenne_matiere("Art",4,100,336)
            sp=calculer_moyenne_matiere("Sport",1,100,379)
            inf=calculer_moyenne_matiere("Tamazight",2,100,422)
        elif niveau=="2 Lettres-Philo":
            mat=calculer_moyenne_matiere("Math",2,100,35)
            ph=calculer_moyenne_matiere("Physique",2,100,78)
            sc=calculer_moyenne_matiere("Science",2,100,121)
            ar=calculer_moyenne_matiere("Arabe",5,100,164)
            isl=calculer_moyenne_matiere("S-Islamique",2,100,207)
            hg=calculer_moyenne_matiere("Histoire-Geo",4,100,250)
            en=calculer_moyenne_matiere("Anglais",3,100,293)
            fr=calculer_moyenne_matiere("Français",3,100,336)
            sp=calculer_moyenne_matiere("Sport",1,100,379)
            inf=calculer_moyenne_matiere("Tamazight",2,100,422)
            tech=calculer_moyenne_matiere("Art",1,100,465)
            cvl=calculer_moyenne_matiere("Philosophie",1,100,508)
        elif niveau=="3 EG":
            mat=calculer_moyenne_matiere("Math",5,100,35)
            ph=calculer_moyenne_matiere("Comptabilité",6,100,78)
            sc=calculer_moyenne_matiere("EG",5,100,121)
            ar=calculer_moyenne_matiere("Droit",2,100,164)
            isl=calculer_moyenne_matiere("S-Islamique",2,100,207)
            hg=calculer_moyenne_matiere("Histoire-Geo",4,100,250)
            en=calculer_moyenne_matiere("Anglais",2,100,293)
            fr=calculer_moyenne_matiere("Français",2,100,336)
            sp=calculer_moyenne_matiere("Sport",1,100,379)
            inf=calculer_moyenne_matiere("Tamazight",2,100,422)
            cvl=calculer_moyenne_matiere("Arabe",3,100,465)
            tech=calculer_moyenne_matiere("Philosophie",2,100,508)
        elif niveau=="3 Science":
            mat=calculer_moyenne_matiere("Math",5,100,35)
            ph=calculer_moyenne_matiere("Physique",5,100,78)
            sc=calculer_moyenne_matiere("Science",6,100,121)
            ar=calculer_moyenne_matiere("Arabe",3,100,164)
            isl=calculer_moyenne_matiere("S-Islamique",2,100,207)
            hg=calculer_moyenne_matiere("Histoire-Geo",2,100,250)
            en=calculer_moyenne_matiere("Anglais",2,100,293)
            fr=calculer_moyenne_matiere("Français",2,100,336)
            sp=calculer_moyenne_matiere("Sport",1,100,379)
            inf=calculer_moyenne_matiere("Tamazight",2,100,422)
            tech=calculer_moyenne_matiere("Philosophie",2,100,465)       
        elif niveau=="3 Math-tech":
            mat=calculer_moyenne_matiere("Math",6,100,35)
            ph=calculer_moyenne_matiere("Physique",6,100,78)
            sc=calculer_moyenne_matiere("Technologie",7,100,121)
            ar=calculer_moyenne_matiere("Arabe",2,100,164)
            isl=calculer_moyenne_matiere("S-Islamique",2,100,207)
            hg=calculer_moyenne_matiere("Histoire-Geo",2,100,250)
            en=calculer_moyenne_matiere("Anglais",2,100,293)
            fr=calculer_moyenne_matiere("Français",2,100,336)
            sp=calculer_moyenne_matiere("Sport",1,100,379)
            inf=calculer_moyenne_matiere("Tamazight",2,100,422)
            tech=calculer_moyenne_matiere("Philosophie",2,100,465)
        elif niveau=="3 Math":
            mat=calculer_moyenne_matiere("Math",7,100,35)
            ph=calculer_moyenne_matiere("Physique",6,100,78)
            sc=calculer_moyenne_matiere("Science",2,100,121)
            ar=calculer_moyenne_matiere("Arabe",3,100,164)
            isl=calculer_moyenne_matiere("S-Islamique",2,100,207)
            hg=calculer_moyenne_matiere("Histoire-Geo",2,100,250)
            en=calculer_moyenne_matiere("Anglais",2,100,293)
            fr=calculer_moyenne_matiere("Français",2,100,336)
            sp=calculer_moyenne_matiere("Sport",1,100,379)
            inf=calculer_moyenne_matiere("Tamazight",2,100,422)
            tech=calculer_moyenne_matiere("Philosophie",2,100,465)
        elif niveau=="3 Langues":
            mat=calculer_moyenne_matiere("Math",2,100,35)
            ph=calculer_moyenne_matiere("Arabe",5,100,78)
            sc=calculer_moyenne_matiere("Anglais",5,100,121)
            ar=calculer_moyenne_matiere("Langue 3",4,100,164)
            isl=calculer_moyenne_matiere("S-Islamique",2,100,207)
            hg=calculer_moyenne_matiere("Histoire-Geo",3,100,250)
            en=calculer_moyenne_matiere("Français",5,100,293)
            fr=calculer_moyenne_matiere("Philosophie",4,100,336)
            sp=calculer_moyenne_matiere("Sport",1,100,379)
            inf=calculer_moyenne_matiere("Tamazight",2,100,422)
        elif niveau=="3 Lettres-Philo":
            mat=calculer_moyenne_matiere("Math",2,100,35)
            ph=calculer_moyenne_matiere("Arabe",6,100,78)
            sc=calculer_moyenne_matiere("Français",3,100,121)
            ar=calculer_moyenne_matiere("Philosophie",6,100,164)
            isl=calculer_moyenne_matiere("S-Islamique",2,100,207)
            hg=calculer_moyenne_matiere("Histoire-Geo",4,100,250)
            en=calculer_moyenne_matiere("Anglais",3,100,293)
            fr=calculer_moyenne_matiere("Sport",1,100,379)
            sp=calculer_moyenne_matiere("Tamazight",2,100,336)
        moy=tk.Button(mn,text="Calculer moyenne",font=("Arial"),command=calculermoyenne,bg="red",fg="black",cursor="hand2")
        moy.place(x=15,y=565)
    confe=tk.Button(mn,text="Confirmer",command=conf,font=("Arial",20),bg="#1c9be6",cursor="hand2")
    confe.place(x=600,y=190)
    def closepar():
        par.place_forget()
        nivea.place_forget()
        nivlab.place_forget()
        confe.place_forget()
        closebtf.place_forget()
    closebtf=tk.Button(mn,image=closebt,command=closepar,cursor="hand2")
    closebtf.place(x=708,y=8)
setb=tk.Button(mn,image=sfl,command=parametres,cursor="hand2")
setb.place(x=708,y=8)
moyerrer=tk.Label(mn,text="",font=("Arial",12),bg="red",fg="white")
moyerrer.place(x=12,y=15)
moyerrer.place_forget()
mn.mainloop()