import pandas as pd
from sqlalchemy import create_engine

# Chemin vers votre fichier CSV
csv_file = 'en.openfoodfacts.org.products.csv'

# Connexion à la base de données MySQL
db_url = "mysql+pymysql://root:@localhost:3306/openfoodfact"
engine = create_engine(db_url)

# Lire un petit échantillon du fichier pour vérifier les colonnes disponibles
df_sample = pd.read_csv(csv_file, sep='\t', nrows=5, low_memory=False)
print("Colonnes disponibles dans le fichier CSV :", df_sample.columns)

# Liste des colonnes que vous souhaitez extraire (adaptez cette liste après avoir vu les colonnes réelles)
selected_columns = [
    'code', 'product_name', 'brands', 'categories', 'nutrition_grade',
    'energy_kcal_100g', 'fat_100g', 'saturated_fat_100g', 'unsaturated_fat_100g',
    'monounsaturated_fat_100g', 'polyunsaturated_fat_100g', 'trans_fat_100g',
    'carbohydrates_100g', 'sugars_100g', 'added_sugars_100g', 'starch_100g',
    'fiber_100g', 'proteins_100g', 'cholesterol_100g', 'sodium_100g', 'salt_100g',
    'added_salt_100g', 'glycemic_index_100g', 'vitamin_a_100g', 'vitamin_c_100g',
    'vitamin_d_100g', 'vitamin_e_100g', 'vitamin_k_100g', 'vitamin_b1_100g',
    'vitamin_b2_100g', 'vitamin_b6_100g', 'vitamin_b9_100g', 'vitamin_b12_100g',
    'calcium_100g', 'iron_100g', 'magnesium_100g', 'potassium_100g', 'zinc_100g',
    'allergens', 'allergens_en', 'traces', 'traces_en'
]

# Lire et traiter le fichier CSV en morceaux (chunks)
chunksize = 100000  # Lire 100 000 lignes à la fois

for chunk in pd.read_csv(csv_file, sep='\t', chunksize=chunksize, low_memory=False, on_bad_lines='skip'):
    # Filtrer les colonnes disponibles dans le chunk
    available_columns = [col for col in selected_columns if col in chunk.columns]
    chunk_filtered = chunk[available_columns]

    # Insérer le chunk dans la base de données MySQL
    chunk_filtered.to_sql('products', con=engine, if_exists='append', index=False)

    print(f"Chunk de {len(chunk_filtered)} lignes inséré avec succès.")
