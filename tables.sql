CREATE TABLE diets (
  diet_id SERIAL PRIMARY KEY,
  diet_name VARCHAR(255) NOT NULL,
  carb_limit FLOAT,
  fat_limit FLOAT,
  protein_limit FLOAT,
  calorie_limit FLOAT
);

CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  diet_id SERIAL REFERENCES diets(diet_id)
);

CREATE TABLE products (
  product_id SERIAL PRIMARY KEY,
  code VARCHAR(255) UNIQUE NOT NULL,
  product_name VARCHAR(255) NOT NULL,
  brands VARCHAR(255),
  categories VARCHAR(255),
  nutrition_grade CHAR(1),
  energy_kcal_100g FLOAT,
  fat_100g FLOAT,
  saturated_fat_100g FLOAT,
  unsaturated_fat_100g FLOAT,
  monounsaturated_fat_100g FLOAT,
  polyunsaturated_fat_100g FLOAT,
  trans_fat_100g FLOAT,
  carbohydrates_100g FLOAT,
  sugars_100g FLOAT,
  added_sugars_100g FLOAT,
  starch_100g FLOAT,
  fiber_100g FLOAT,
  proteins_100g FLOAT,
  cholesterol_100g FLOAT,
  sodium_100g FLOAT,
  salt_100g FLOAT,
  added_salt_100g FLOAT,
  glycemic_index_100g FLOAT,
  vitamin_a_100g FLOAT,
  vitamin_c_100g FLOAT,
  vitamin_d_100g FLOAT,
  vitamin_e_100g FLOAT,
  vitamin_k_100g FLOAT,
  vitamin_b1_100g FLOAT,
  vitamin_b2_100g FLOAT,
  vitamin_b6_100g FLOAT,
  vitamin_b9_100g FLOAT,
  vitamin_b12_100g FLOAT,
  calcium_100g FLOAT,
  iron_100g FLOAT,
  magnesium_100g FLOAT,
  potassium_100g FLOAT,
  zinc_100g FLOAT,
  allergens TEXT,
  allergens_en TEXT,
  traces TEXT,
  traces_en TEXT
);


