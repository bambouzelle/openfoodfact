import pymysql
import random

# Informations de connexion à la base de données MySQL
db_config = {
    'host': 'localhost',
    'user': 'user',
    'password': 'userpassword',
    'database': 'openfoodfact'
}

# Fonction pour se connecter à la base de données
def connect_to_db():
    try:
        connection = pymysql.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )
        return connection
    except pymysql.MySQLError as e:
        print(f"Erreur de connexion à la base de données : {e}")
        return None

# Fonction pour récupérer les informations de régime pour un utilisateur donné
def get_diet_limits_for_user(connection, user_name):
    with connection.cursor() as cursor:
        query = """
        SELECT diets.carb_limit, diets.fat_limit, diets.protein_limit, diets.calorie_limit
        FROM users
        JOIN diets ON users.diet_id = diets.diet_id
        WHERE users.name = %s
        """
        cursor.execute(query, (user_name,))
        return cursor.fetchone()

# Fonction pour récupérer des produits qui respectent les limites du régime
def get_products_for_diet(connection, diet_limits):
    carb_limit, fat_limit, protein_limit, calorie_limit = diet_limits
    with connection.cursor() as cursor:
        query = """
        SELECT product_name, product_quantity, `energy-kcal_100g`, `carbohydrates_100g`, `fat_100g`, `proteins_100g`,
               (product_quantity / 100) * `energy-kcal_100g` AS total_calories
        FROM products
        WHERE `carbohydrates_100g` <= %s
        AND `fat_100g` <= %s
        AND `proteins_100g` <= %s
        AND `energy-kcal_100g` <= %s
        ORDER BY RAND()
        """
        cursor.execute(query, (carb_limit, fat_limit, protein_limit, calorie_limit))
        return cursor.fetchall()

# Fonction pour assembler une journée alimentaire avec un total calorique entre 1600 et 3200 calories
def assemble_meal_day(products, min_calories=1600, max_calories=3200):
    total_calories = 0
    meal_plan = []

    for product in products:
        product_name, product_quantity, calories_per_100g, carbs, fats, proteins, total_product_calories = product

        # Vérifier si les calories du produit sont valides (pas None)
        if total_product_calories is not None and total_calories + total_product_calories <= max_calories:
            meal_plan.append(product)
            total_calories += total_product_calories

        # Si on a atteint un total de calories entre les limites souhaitées, arrêter
        if min_calories <= total_calories <= max_calories:
            break

    return meal_plan, total_calories

# Fonction principale
def main():
    connection = connect_to_db()
    if connection:
        print("Connexion à la base de données réussie !")

        # Demander le nom de l'utilisateur
        user_name = input("Entrez le nom de l'utilisateur : ")

        # Récupérer les limites de régime pour l'utilisateur
        diet_limits = get_diet_limits_for_user(connection, user_name)
        
        if diet_limits:
            print(f"Régime trouvé pour {user_name} : {diet_limits}")

            # Récupérer les produits correspondant au régime de l'utilisateur
            products = get_products_for_diet(connection, diet_limits)

            # Assembler une journée alimentaire
            meal_plan, total_calories = assemble_meal_day(products)

            if meal_plan:
                print(f"Journée alimentaire assemblée avec un total de {total_calories:.2f} calories :")
                for product in meal_plan:
                    print(f"Produit: {product[0]}, Quantité : {product[1]}g, Calories Totales : {product[6]:.2f} kcal")
            else:
                print("Impossible d'assembler une journée alimentaire avec les critères donnés.")
        else:
            print(f"Aucun régime trouvé pour l'utilisateur {user_name}.")

        connection.close()

# Exécuter le script
if __name__ == "__main__":
    main()
