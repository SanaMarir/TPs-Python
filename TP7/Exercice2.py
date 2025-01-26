import os
from datetime import datetime
import math

def main():
# 1. Afficher le répertoire courant
    current_directory = os.getcwd()
    print(f"Répertoire courant : {current_directory}")
    
# 2. Afficher la date et l'heure actuelles
    current_time = datetime.now()
    print(f"Date et heure actuelles : {current_time}")
    
# 3. Calculer la racine carrée d'un nombre donné par l'utilisateur
    try:
        number = float(input("Entrez un nombre pour calculer sa racine carrée : "))
        if number < 0:
            raise ValueError("La racine carrée d'un nombre négatif n'est pas définie dans les réels.")
        sqrt_result = math.sqrt(number)
        print(f"La racine carrée de {number} est : {sqrt_result}")
    except ValueError as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    main()
