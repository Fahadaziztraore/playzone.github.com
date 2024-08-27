from tkinter import *

def submit():
    DataT = DataTitle.get()
    ImageS = ImageSrc.get()
    Taill = Taille.get()
    Stat = status_var.get()
    Ver = Version.get()
    Categ = category_var.get()
    lien = LienD.get()
    nom_fichier = fichier_var.get()  # Récupération du nom de fichier choisi

    un = '\n\n\t\t<div class="game" data-title="'+DataT+'">\n\t\t\t<div class="droite">'
    deux = '\n\t\t\t\t<img src="'+ImageS+'" width="70" alt="'+DataT+'">'+'\n\t\t\t</div>\n\t\t\t<div class="game-details">'
    trois = '\n\t\t\t\t<h2>'+DataT+'</h2>'
    quatr = '\n\t\t\t\t<p>Taille : '+Taill+'</p>'
    cinq = '\n\t\t\t\t<p>Status : '+Stat+'</p>'
    six = '\n\t\t\t\t<p>Version : '+Ver+'     Type : '+Categ+'</p>\n\n\t\t\t</div>'
    sept = '\n\t\t\t<a href="'+lien+'" download style="font-size: 5px; display: inline-block; text-align: left;">\n\t\t\t\t<img src="PhotoImage/download.png" width="50" height="50" alt="Telecharger">\n\t\t</a>\n\t\t</div>'

    all = un + deux + trois + quatr + cinq + six + sept

    # Utilisation du nom de fichier choisi dans le menu déroulant
    with open(nom_fichier + '.txt', 'a') as h:
        h.write(all)

    # Réinitialiser les champs après l'enregistrement
    DataTitle.delete(0, END)
    ImageSrc.delete(0, END)
    Taille.delete(0, END)
    status_var.set("choisir...")
    Version.delete(0, END)
    category_var.set("choisir...")
    LienD.delete(0, END)

m = Tk()
m['bg'] = 'blue'
m.geometry('600x500+500+300')
frame = Frame(m).place(x=20, y=40)

LabelText0 = Label(m, font=('arial', 20), bg='blue', fg='white', text='Nom du fichier').grid(column=0, row=0)
fichier_var = StringVar(m)
fichier_var.set("action")  # Valeur par défaut
NomFichier = OptionMenu(m, fichier_var, "action", "strategie", "logiciel")
NomFichier.config(font=('arial', 20), bg='blue', fg='white', width=10)
NomFichier.grid(column=1, row=0)

LabelText1 = Label(m, font=('arial', 20), bg='blue', fg='white', text='Nom de recherche').grid(column=0, row=1)
DataTitle = Entry(m, font=('arial', 20), bg='blue', fg='white', width=10)
DataTitle.grid(column=1, row=1)

LabelText2 = Label(m, font=('arial', 20), bg='blue', fg='white', text='Lien de l\'icone du jeu').grid(column=0, row=2)
ImageSrc = Entry(m, font=('arial', 20), bg='blue', fg='white', width=10)
ImageSrc.grid(column=1, row=2)

LabelText4 = Label(m, font=('arial', 20), bg='blue', fg='white', text='Taille en (Mo)').grid(column=0, row=4)
Taille = Entry(m, font=('arial', 20), bg='blue', fg='white', width=10)
Taille.grid(column=1, row=4)

LabelText5 = Label(m, font=('arial', 20), bg='blue', fg='white', text='Status').grid(column=0, row=6)
status_var = StringVar(m)
status_var.set("choisir...")
Status = OptionMenu(m, status_var, "connection", "hors connection")
Status.config(font=('arial', 20), bg='blue', fg='white', width=10)
Status.grid(column=1, row=6)

LabelText7 = Label(m, font=('arial', 20), bg='blue', fg='white', text='Categories').grid(column=0, row=8)
category_var = StringVar(m)
category_var.set("choisir...")
Categorie = OptionMenu(m, category_var, "action", "aventure", "strategie", "epée", "logiciel", "simulation")
Categorie.config(font=('arial', 20), bg='blue', fg='white', width=10)
Categorie.grid(column=1, row=8)

LabelText6 = Label(m, font=('arial', 20), bg='blue', fg='white', text='Version').grid(column=0, row=7)
Version = Entry(m, font=('arial', 20), bg='blue', fg='white', width=10)
Version.grid(column=1, row=7)

LabelText7 = Label(m, font=('arial', 20), bg='blue', fg='white', text='Lien de telechargement (http ou...)').grid(column=0, row=9)
LienD = Entry(m, font=('arial', 20), bg='blue', fg='white', width=10)
LienD.grid(column=1, row=9)

Soumettre = Button(m, command=submit, font=('arial', 20), bg='green', fg='white', text='Soumettre').grid(column=1, row=10)

mainloop()
