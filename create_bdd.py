import pandas as pd

# Chemin vers votre fichier CSV
csv_file = 'en.openfoodfacts.org.products.csv'

# Lire le CSV avec pandas pour obtenir les colonnes
df = pd.read_csv(csv_file, nrows=0)  # On ne lit que les en-têtes pour les colonnes

# Définir les types de données SQL pour chaque colonne du fichier CSV "products"
custom_sql_types_products = {
    'code': 'VARCHAR(255) UNIQUE NOT NULL',
    'product_name': 'VARCHAR(255) NOT NULL',
    'brands': 'VARCHAR(255)',
    'categories': 'VARCHAR(255)',
    'nutrition_grade': 'CHAR(1)',
    'energy_kcal_100g': 'FLOAT',
    'proteins_100g': 'FLOAT',
    'carbohydrates_100g': 'FLOAT',
    'sugars_100g': 'FLOAT',
    'fat_100g': 'FLOAT',
    'saturated_fat_100g': 'FLOAT',
    'fiber_100g': 'FLOAT',
    'sodium_100g': 'FLOAT',
    'fruits_vegetables_nuts_100g': 'FLOAT'
}

# Définir les types de données SQL pour la table des utilisateurs "users"
custom_sql_types_users = {
    'user_id': 'SERIAL PRIMARY KEY',
    'name': 'VARCHAR(255) NOT NULL',
    'diet_id': 'INT REFERENCES diets(diet_id)'
}

# Définir les types de données SQL pour la table des régimes alimentaires "diets"
custom_sql_types_diets = {
    'diet_id': 'SERIAL PRIMARY KEY',
    'diet_name': 'VARCHAR(255) NOT NULL',
    'carb_limit': 'FLOAT',
    'fat_limit': 'FLOAT',
    'protein_limit': 'FLOAT',
    'calorie_limit': 'FLOAT'
}

# Fonction pour générer le script SQL
def generate_sql_script(table_name, custom_sql_types):
    sql_script = f"CREATE TABLE {table_name} (\n"
    
    for col, col_type in custom_sql_types.items():
        sql_script += f"  {col} {col_type},\n"
    
    # Enlever la dernière virgule et fermer la table
    sql_script = sql_script.rstrip(',\n') + "\n);\n"
    
    return sql_script

# Générer les scripts SQL pour chaque table
sql_script_products = generate_sql_script('products', custom_sql_types_products)
sql_script_users = generate_sql_script('users', custom_sql_types_users)
sql_script_diets = generate_sql_script('diets', custom_sql_types_diets)

# Écrire tous les scripts dans un seul fichier SQL
sql_file = 'create_all_tables_float.sql'
with open(sql_file, 'w') as file:
    file.write(sql_script_diets)  # Commencer par la table des régimes pour la contrainte de clé étrangère
    file.write("\n")
    file.write(sql_script_users)
    file.write("\n")
    file.write(sql_script_products)

print(f"Le script SQL pour toutes les tables avec des nombres à virgule (FLOAT) a été généré et sauvegardé dans {sql_file}.")
