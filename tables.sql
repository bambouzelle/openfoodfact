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
  code VARCHAR(255) UNIQUE NOT NULL,
  product_name VARCHAR(255) NOT NULL,
  brands VARCHAR(255),
  categories VARCHAR(255),
  nutrition_grade CHAR(1),
  energy_kcal_100g FLOAT,
  proteins_100g FLOAT,
  carbohydrates_100g FLOAT,
  sugars_100g FLOAT,
  fat_100g FLOAT,
  saturated_fat_100g FLOAT,
  fiber_100g FLOAT,
  sodium_100g FLOAT,
  fruits_vegetables_nuts_100g FLOAT
);
