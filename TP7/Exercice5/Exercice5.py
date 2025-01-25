import pandas as pd

  
data = pd.read_csv("C:/Users/Admin/Desktop/TP7/employees.csv")
print("Données chargées avec succès.")
        
        
print("\nLes cinq premières lignes du fichier :")
print(data.head())
        
        
if 'Age' in data.columns:
    mean_age = data['Age'].mean()
    print(f"\nL'âge moyen des employés est : {mean_age:.2f} ans")
else:
    print("\nLa colonne 'Age' est absente du fichier.")


