import tkinter as tk
from tkinter import ttk
import pyperclip
from PIL import Image, ImageTk

# Dictionnaire des codes de triche Sims 4 regroupés par catégorie
sims4_cheat_codes = {
    "Financiers": {
        "motherlode": "Ajoute 50 000 simflouz à votre compte de ménage",
        "rosebud": "Ajoute 1 000 simflouz à votre compte de ménage",
        "kaching": "Ajoute 1 000 simflouz à votre compte de ménage",
        "money 100000": "Définit les simflouz de votre ménage à 100 000",
        "money 200000": "Définit les simflouz de votre ménage à 200 000",
        "money 300000": "Définit les simflouz de votre ménage à 300 000",
        "money 9900000": "Définit les simflouz de votre ménage à 9 900 000",
        "money 9999999": "Définit les simflouz de votre ménage à 9 999 999"
    },
    "Immobilier": {
        "freerealestate on": "Rend toutes les maisons gratuites",
        "freerealestate off": "Désactive le code précédent"
    },
    "Construction": {
        "bb.moveobjects on": "Permet de placer des objets n'importe où",
        "bb.moveobjects off": "Désactive le code précédent",
        "bb.showhiddenobjects": "Affiche les objets cachés dans le mode construction",
        "bb.ignoregameplayunlocksentitlement": "Débloque tous les objets de carrière dans le mode construction",
        "bb.enablefreebuild": "Permet de construire n'importe où"
    },
    "Sim": {
        "resetSim [prenom] [nom]": "Réinitialise le Sim spécifié",
        "cas.fulleditmode": "Permet de modifier entièrement les Sims en utilisant le CAS",
        "sims.give_satisfaction_points [nombre]": "Donne le nombre spécifié de points de satisfaction au Sim actif",
        "sims.add_buff Buff_Motives_Hunger_Starving": "Affame le Sim actif",
        "sims.remove_all_buffs": "Supprime tous les buffs du Sim actif",
        "sims.fill_all_commodities": "Remplit toutes les commodités du Sim actif"
    },
    "Compétences": {
        "stats.set_skill_level Major_Acting 10": "Définit le niveau de compétence d'acteur au maximum",
        "stats.set_skill_level Major_Baking 10": "Définit le niveau de compétence de pâtisserie au maximum",
        "stats.set_skill_level Major_Bartending 10": "Définit le niveau de compétence de mixologie au maximum",
        "stats.set_skill_level Major_Charisma 10": "Définit le niveau de compétence de charisme au maximum",
        "stats.set_skill_level Major_Comedy 10": "Définit le niveau de compétence de comédie au maximum",
        "stats.set_skill_level Major_DJMixing 10": "Définit le niveau de compétence de DJ au maximum",
        "stats.set_skill_level Major_Fishing 10": "Définit le niveau de compétence de pêche au maximum",
        "stats.set_skill_level Major_Fitness 10": "Définit le niveau de compétence de fitness au maximum",
        "stats.set_skill_level Major_Gardening 10": "Définit le niveau de compétence de jardinage au maximum",
        "stats.set_skill_level Major_GourmetCooking 10": "Définit le niveau de compétence de cuisine gastronomique au maximum",
        "stats.set_skill_level Major_Guitar 10": "Définit le niveau de compétence de guitare au maximum",
        "stats.set_skill_level Major_Handiness 10": "Définit le niveau de compétence de bricolage au maximum",
        "stats.set_skill_level Major_Herbalism 10": "Définit le niveau de compétence d'herboristerie au maximum",
        "stats.set_skill_level Major_Logic 10": "Définit le niveau de compétence de logique au maximum",
        "stats.set_skill_level Major_Mischief 10": "Définit le niveau de compétence de malice au maximum",
        "stats.set_skill_level Major_Painting 10": "Définit le niveau de compétence de peinture au maximum",
        "stats.set_skill_level Major_Physician 10": "Définit le niveau de compétence de médecin au maximum",
        "stats.set_skill_level Major_Photography 10": "Définit le niveau de compétence de photographie au maximum",
        "stats.set_skill_level Major_Piano 10": "Définit le niveau de compétence de piano au maximum",
        "stats.set_skill_level Major_Programming 10": "Définit le niveau de compétence de programmation au maximum",
        "stats.set_skill_level Major_RocketScience 10": "Définit le niveau de compétence de science spatiale au maximum",
        "stats.set_skill_level Major_VideoGaming 10": "Définit le niveau de compétence de jeux vidéo au maximum",
        "stats.set_skill_level Major_Violin 10": "Définit le niveau de compétence de violon au maximum",
        "stats.set_skill_level Major_Wellness 10": "Définit le niveau de compétence de bien-être au maximum",
        "stats.set_skill_level Major_Writing 10": "Définit le niveau de compétence d'écriture au maximum"
    },
    "Carrière": {
        "careers.promote Actor": "Promeut le Sim actif dans la carrière d'acteur",
        "careers.demote Actor": "Rétrograde le Sim actif dans la carrière d'acteur",
        "careers.promote Astronaut": "Promeut le Sim actif dans la carrière d'astronaute",
        "careers.demote Astronaut": "Rétrograde le Sim actif dans la carrière d'astronaute",
        "careers.promote Athlete": "Promeut le Sim actif dans la carrière d'athlète",
        "careers.demote Athlete": "Rétrograde le Sim actif dans la carrière d'athlète",
        "careers.promote Business": "Promeut le Sim actif dans la carrière de business",
        "careers.demote Business": "Rétrograde le Sim actif dans la carrière de business",
        "careers.promote CivilDesigner": "Promeut le Sim actif dans la carrière de designer civil",
        "careers.demote CivilDesigner": "Rétrograde le Sim actif dans la carrière de designer civil",
        "careers.promote Conservationist": "Promeut le Sim actif dans la carrière de conservationniste",
        "careers.demote Conservationist": "Rétrograde le Sim actif dans la carrière de conservationniste",
        "careers.promote Critic": "Promeut le Sim actif dans la carrière de critique",
        "careers.demote Critic": "Rétrograde le Sim actif dans la carrière de critique",
        "careers.promote Culinary": "Promeut le Sim actif dans la carrière culinaire",
        "careers.demote Culinary": "Rétrograde le Sim actif dans la carrière culinaire",
        "careers.promote Detective": "Promeut le Sim actif dans la carrière de détective",
        "careers.demote Detective": "Rétrograde le Sim actif dans la carrière de détective",
        "careers.promote Doctor": "Promeut le Sim actif dans la carrière de docteur",
        "careers.demote Doctor": "Rétrograde le Sim actif dans la carrière de docteur",
        "careers.promote Education": "Promeut le Sim actif dans la carrière d'éducation",
        "careers.demote Education": "Rétrograde le Sim actif dans la carrière d'éducation",
        "careers.promote Engineer": "Promeut le Sim actif dans la carrière d'ingénieur",
        "careers.demote Engineer": "Rétrograde le Sim actif dans la carrière d'ingénieur",
        "careers.promote Entertainer": "Promeut le Sim actif dans la carrière d'animateur",
        "careers.demote Entertainer": "Rétrograde le Sim actif dans la carrière d'animateur",
        "careers.promote Freelancer": "Promeut le Sim actif dans la carrière de freelance",
        "careers.demote Freelancer": "Rétrograde le Sim actif dans la carrière de freelance",
        "careers.promote Gardener": "Promeut le Sim actif dans la carrière de jardinier",
        "careers.demote Gardener": "Rétrograde le Sim actif dans la carrière de jardinier",
        "careers.promote InteriorDecorator": "Promeut le Sim actif dans la carrière de décorateur d'intérieur",
        "careers.demote InteriorDecorator": "Rétrograde le Sim actif dans la carrière de décorateur d'intérieur",
        "careers.promote Law": "Promeut le Sim actif dans la carrière juridique",
        "careers.demote Law": "Rétrograde le Sim actif dans la carrière juridique",
        "careers.promote Military": "Promeut le Sim actif dans la carrière militaire",
        "careers.demote Military": "Rétrograde le Sim actif dans la carrière militaire",
        "careers.promote Painter": "Promeut le Sim actif dans la carrière de peintre",
        "careers.demote Painter": "Rétrograde le Sim actif dans la carrière de peintre",
        "careers.promote Scientist": "Promeut le Sim actif dans la carrière de scientifique",
        "careers.demote Scientist": "Rétrograde le Sim actif dans la carrière de scientifique",
        "careers.promote Scout": "Promeut le Sim actif dans la carrière de scout",
        "careers.demote Scout": "Rétrograde le Sim actif dans la carrière de scout",
        "careers.promote SecretAgent": "Promeut le Sim actif dans la carrière d'agent secret",
        "careers.demote SecretAgent": "Rétrograde le Sim actif dans la carrière d'agent secret",
        "careers.promote SocialMedia": "Promeut le Sim actif dans la carrière des réseaux sociaux",
        "careers.demote SocialMedia": "Rétrograde le Sim actif dans la carrière des réseaux sociaux",
        "careers.promote StyleInfluencer": "Promeut le Sim actif dans la carrière de styliste",
        "careers.demote StyleInfluencer": "Rétrograde le Sim actif dans la carrière de styliste",
        "careers.promote TechGuru": "Promeut le Sim actif dans la carrière de guru de la technologie",
        "careers.demote TechGuru": "Rétrograde le Sim actif dans la carrière de guru de la technologie",
        "careers.promote Writer": "Promeut le Sim actif dans la carrière d'écrivain",
        "careers.demote Writer": "Rétrograde le Sim actif dans la carrière d'écrivain"
    },
    "Divers": {
        "testingcheats true": "Active les codes de triche",
        "testingcheats false": "Désactive les codes de triche",
        "death.toggle [true/false]": "Active ou désactive la mort des Sims",
        "headlineeffects [on/off]": "Active ou désactive les effets de titre (plumbobs, bulles de pensée, etc.)"
    }
}

# Fonction pour mettre à jour les codes de triche disponibles
def mettre_a_jour_code_combo(event):
    categorie = categorie_combo.get()
    codes = list(sims4_cheat_codes.get(categorie, {}).keys())
    code_triche_combo['values'] = codes
    if codes:
        code_triche_combo.current(0)
        mettre_a_jour_description(None)

# Fonction pour mettre à jour la description du code de triche sélectionné
def mettre_a_jour_description(event):
    categorie = categorie_combo.get()
    code = code_triche_combo.get()
    description = sims4_cheat_codes.get(categorie, {}).get(code, "Description non trouvée.")
    description_text.delete(1.0, tk.END)
    description_text.insert(tk.END, description)

# Fonction pour copier le code de triche au presse-papier
def copier_au_presse_papier():
    code = code_triche_combo.get()
    pyperclip.copy(code)
    statut_label.config(text=f"Code '{code}' copié au presse-papier !")

# Fonction pour définir le fond
def set_background(image_path):
    try:
        bg_image = Image.open(image_path)
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(root, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(relwidth=1, relheight=1)
    except FileNotFoundError:
        erreur_label = ttk.Label(root, text="Image de fond non trouvée.")
        erreur_label.place(relwidth=1, relheight=1)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Sims4code")
root.geometry("575x550")
root.iconbitmap("icon.ico")

# Définir le fond 
set_background('bk.png')

# Ajout des widgets dans 'Codes'
categorie_combo = ttk.Combobox(root, values=list(sims4_cheat_codes.keys()))
categorie_combo.bind('<<ComboboxSelected>>', mettre_a_jour_code_combo)
categorie_combo.pack(pady=10, fill='x')

code_triche_combo = ttk.Combobox(root)
code_triche_combo.bind('<<ComboboxSelected>>', mettre_a_jour_description)
code_triche_combo.pack(pady=10, fill='x')

copier_bouton = ttk.Button(root, text="Copier le code", command=copier_au_presse_papier)
copier_bouton.pack(pady=10)

description_text = tk.Text(root, wrap='word', height=4)
description_text.pack(pady=10, expand=True, fill='both')

statut_label = ttk.Label(root, text="")
statut_label.pack(pady=10)

# Instructions pour ouvrir le champ de code dans Les Sims 4
instructions = """
Pour ouvrir le champ de code dans Les Sims 4, vous devez suivre les étapes suivantes :
1. Appuyez sur `Ctrl + Shift + C` sur PC ou sur les quatre gâchettes sur console pour ouvrir la boîte de code.

Maintenant, vous pouvez entrer n'importe quel code de triche que vous voulez utiliser dans le jeu.
"""
instructions_label = ttk.Label(root, text=instructions)
instructions_label.pack(pady=10)

# Ouvrez une image avec PIL (remplacez 'clavier.png' par le chemin de votre image)
try:
    image = Image.open('clavier.png')
    tk_image = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=tk_image)
    image_label.pack(pady=10)
except FileNotFoundError:
    erreur_label = ttk.Label(root, text="Image non trouvée. Assurez-vous que 'clavier.png' est dans le bon répertoire.")
    erreur_label.pack(pady=10)

# Lancement de la boucle principale
root.mainloop()
