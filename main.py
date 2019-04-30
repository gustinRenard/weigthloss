##########################
#Données de l'utilisateur#
##########################

"""
user_taille -> m
user_poids -> kg
user_sexe -> 0 si fille et 1 si mec
user_img_obj -> entre 10 et 15
user_rythme -> entre 0.75 et 1
"""

#Par default
user_taille = 1.79
user_poids = 87.4
user_age = 17
user_sexe = 1
user_img_obj = 10
user_rythme = 1

#Personnalisation
"""
user_taille = float(input("Taille :"))
user_poids = float(input("Poids :"))
user_age = float(input("Age :"))
user_sexe = int(input("Sexe :"))
user_img_obj = int(input("Objectif masse grasse :"))
user_rythme = float(input("Rythme :"))
"""

###################
#Calcul de données#
###################

user_imc = user_poids/(user_taille**2)
user_img_reel = ((1.2*user_imc)+(0.23*user_age)-(10.8*user_sexe)-5.4)/100
user_poids_gras = user_poids*user_img_reel
user_poids_gras_zero = user_poids-user_poids_gras
user_poids_obj = round(user_poids_gras_zero+(user_poids_gras_zero*(user_img_obj/100)),2)
user_poids_loose = round(user_poids-user_poids_obj)

print("\nObjectif :",user_poids_obj,"\nPoids a perdre :",user_poids_loose)

semaine = 0

while user_poids > user_poids_obj:
    semaine += 1
    user_poids_week = round(user_poids*(user_rythme/100),2)
    user_poids = round(user_poids-user_poids_week,2)
    print("\nSemaine :",semaine,"Poids objectif en fin de semaine :",user_poids,"\nPoids a perdre pour reussir l'objectif :",user_poids_week)

print("\nMois :",semaine/4)
print(round(user_poids_loose/(semaine/4),2),"kg/mois")

"""
Gustin Renard
Lundi 29 Avril 2019
"""
