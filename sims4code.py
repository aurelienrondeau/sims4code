import tkinter as tk
from tkinter import ttk
import pyperclip
from PIL import Image, ImageTk
import webbrowser

# Dictionnaire des codes de triche Sims 4 regroupés par catégorie
sims4_cheat_codes = {
    "Financiers": {
        "motherlode": "Ajoute 50 000 simflouz à votre compte de ménage",
        "rosebud": "Ajoute 1 000 simflouz à votre compte de ménage",
        "kaching": "Ajoute 1 000 simflouz à votre compte de ménage",
    },
    "Immobilier": {
        "freerealestate on": "Rend toutes les maisons gratuites",
        "freerealestate off": "Désactive le code précédent",
    },
    "Construction": {
        "bb.moveobjects on": "Permet de placer des objets n'importe où",
        "bb.moveobjects off": "Désactive le code précédent",
        "bb.showhiddenobjects": "Affiche les objets cachés dans le mode construction",
        "bb.ignoregameplayunlocksentitlement": "Débloque tous les objets de carrière dans le mode construction",
    },
    "carrier": {
        "careers.promote": "Ton Sims obtient une promotion",
        "careers.add_career Actor": "Permet d'assigner la carrière de Actor",
        "careers.remove_career Actor": "Supprimer la carrière Actor",
        "careers.retire": "Ton Sims prend sa retraite et reçoit une pension.",
    },
    "relation": {
        "relationships.create_friends_for_sim": "Créer un ami aléatoire",
        "relationship.introduce_sim_to_all_others": "Permet de rencontrer tous les Sims. T'as la flemme d'aller au parc on dirait ?",
    },
    # Ajoutez plus de catégories et de codes de triche ici...
}

def copier_au_presse_papier():
    categorie = categorie_combo.get()
    code = code_triche_combo.get()
    if categorie in sims4_cheat_codes and code in sims4_cheat_codes[categorie]:
        pyperclip.copy(code)
        statut_label.config(text=f"Le code '{code}' a été copié dans le presse-papiers.")
    else:
        statut_label.config(text="Erreur : Sélection invalide.")

def mettre_a_jour_code_combo(event):
    categorie = categorie_combo.get()
    if categorie in sims4_cheat_codes:
        code_triche_combo['values'] = list(sims4_cheat_codes[categorie].keys())
        code_triche_combo.set('')  # Réinitialise la sélection de la liste déroulante des codes de triche

def mettre_a_jour_description(event):
    categorie = categorie_combo.get()
    code = code_triche_combo.get()
    if categorie in sims4_cheat_codes and code in sims4_cheat_codes[categorie]:
        description_text.delete(1.0, tk.END)
        description_text.insert(tk.END, sims4_cheat_codes[categorie][code])
    else:
        description_text.delete(1.0, tk.END)
        description_text.insert(tk.END, "Description non disponible.")

def ouvrir_telechargement():
    webbrowser.open("https://deaderpool-mccc.com/downloads.html")

def set_background(onglet, image_path):
    try:
        bg_image = Image.open(image_path)
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(onglet, image=bg_photo)
        bg_label.image = bg_photo  # keep a reference to avoid garbage collection
        bg_label.place(relwidth=1, relheight=1)
    except FileNotFoundError:
        erreur_label = ttk.Label(onglet, text="Image de fond non trouvée.")
        erreur_label.place(relwidth=1, relheight=1)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Copieur de codes de triche Sims 4")
root.geometry("1024x756")

# Création du widget Notebook (onglets)
notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill="both")

# Création des onglets
onglet1 = ttk.Frame(notebook)
onglet2 = ttk.Frame(notebook)
onglet3 = ttk.Frame(notebook)
onglet4 = ttk.Frame(notebook)
onglet5 = ttk.Frame(notebook)

notebook.add(onglet1, text='Codes')
notebook.add(onglet2, text='MC Command Center')
notebook.add(onglet3, text='UI Cheats Extension')
notebook.add(onglet4, text="TwistedMexi's TOOL")
notebook.add(onglet5, text='Site de mods')

# Définir le fond pour chaque onglet
set_background(onglet1, 'bk.png')
set_background(onglet2, 'bk.png')
set_background(onglet3, 'bk.png')
set_background(onglet4, 'bk.png')
set_background(onglet5, 'bk.png')

# Ajout des widgets dans l'onglet 'Codes'
categorie_combo = ttk.Combobox(onglet1, values=list(sims4_cheat_codes.keys()))
categorie_combo.bind('<<ComboboxSelected>>', mettre_a_jour_code_combo)
categorie_combo.pack(pady=10)

code_triche_combo = ttk.Combobox(onglet1)
code_triche_combo.bind('<<ComboboxSelected>>', mettre_a_jour_description)
code_triche_combo.pack(pady=10)

copier_bouton = ttk.Button(onglet1, text="Copier le code", command=copier_au_presse_papier)
copier_bouton.pack(pady=10)

description_text = tk.Text(onglet1, wrap='word', height=4)
description_text.pack(pady=10, expand=True, fill='both')

statut_label = ttk.Label(onglet1, text="")
statut_label.pack(pady=10)

# Instructions pour ouvrir le champ de code dans Les Sims 4
instructions = """
Pour ouvrir le champ de code dans Les Sims 4, vous devez suivre les étapes suivantes :
1. Appuyez sur `Ctrl + Shift + C` sur PC ou sur les quatre gâchettes sur console pour ouvrir la boîte de code.

Maintenant, vous pouvez entrer n'importe quel code de triche que vous voulez utiliser dans le jeu.
"""
instructions_label = ttk.Label(onglet1, text=instructions)
instructions_label.pack(pady=10)

# Ouvrez une image avec PIL (remplacez 'clavier.png' par le chemin de votre image)
try:
    image = Image.open('clavier.png')
    tk_image = ImageTk.PhotoImage(image)
    image_label = tk.Label(onglet1, image=tk_image)
    image_label.pack(pady=10)
except FileNotFoundError:
    erreur_label = ttk.Label(onglet1, text="Image non trouvée. Assurez-vous que 'clavier.png' est dans le bon répertoire.")
    erreur_label.pack(pady=10)

# Ajout des widgets dans l'onglet 'MC Command Center'
description_mccc = """
Le MC Command Center est un mod pour Les Sims 4 créé par Deaderpool. Ce mod est très populaire dans la communauté des Sims 4 et il est traduit en français.

Voici quelques détails sur ce mod :

Régler/Paramétrer le jeu : Ce mod vous permet de régler et de paramétrer votre jeu dans ses moindres détails de façon simple et ludique. Il offre une plus grande maîtrise et fonctionnalité sur tout, depuis la tenue d’un Sim (y compris les PNJ) jusqu’à la gestion de la grossesse dans le jeu.
Fin des codes compliqués : Avec ce mod, fini les longues lignes de codes compliquées à retenir ou à entasser dans un fichier word.
Modification des relations entre les Sims : Vous n’avez plus besoin de passer trois heures à modifier les relations entre les Sims pour créer une histoire réaliste comme vous l’imaginiez. Le MC Command Center s’occupe de tout.
Installation et utilisation simples : Pour installer le MCCC dans votre dossier mods, il suffit de suivre les explications sur l’installation de mods dans Les Sims 4. Son utilisation est simple. Cliquez donc sur un sims et vous verrez apparaître le symbole du mod.
Traduction en français : Le mod est totalement traduit en français, ce qui facilite son utilisation.
Configuration du Sim : Vous pouvez configurer votre Sim à votre convenance. Par exemple, si vous souhaitez qu’il soit un pianiste de renom mais n’avez pas envie de monter sa compétence, en quelques clics c’est fait.
Suppression d’un Sim : Une des commandes qui change la vie est le fait de pouvoir directement en jeu "Supprimer un Sim".
En somme, le MC Command Center est un outil précieux pour personnaliser votre expérience de jeu et ajouter de nouvelles fonctionnalités.
"""

try:
    logo_mccc = Image.open('logo1.png')
    logo_mccc_tk = ImageTk.PhotoImage(logo_mccc)
    logo_label = tk.Label(onglet2, image=logo_mccc_tk)
    logo_label.pack(pady=10)
except FileNotFoundError:
    erreur_label_mccc = ttk.Label(onglet2, text="Image non trouvée. Assurez-vous que 'logo1.png' est dans le bon répertoire.")
    erreur_label_mccc.pack(pady=10)

description_mccc_label = tk.Text(onglet2, wrap='word', height=20)
description_mccc_label.insert(tk.END, description_mccc)
description_mccc_label.config(state=tk.DISABLED)
description_mccc_label.pack(pady=10, expand=True, fill='both')

telechargement_bouton = ttk.Button(onglet2, text="Téléchargement", command=ouvrir_telechargement)
telechargement_bouton.pack(pady=10)

# Lancement de la boucle principale
root.mainloop()
