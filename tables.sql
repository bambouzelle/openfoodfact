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
  diet_id INT,
  FOREIGN KEY (diet_id) REFERENCES diets(diet_id)
);

-- INSERTION DIET
-- Régime Cétogène (Keto)
INSERT INTO diets (diet_name, carb_limit, fat_limit, protein_limit, calorie_limit)
VALUES ('Cétogène', 50, 165, 75, 2000);

-- Régime Low-Carb
INSERT INTO diets (diet_name, carb_limit, fat_limit, protein_limit, calorie_limit)
VALUES ('Low-Carb', 100, 100, 80, 1800);

-- Régime Sportif
INSERT INTO diets (diet_name, carb_limit, fat_limit, protein_limit, calorie_limit)
VALUES ('Sportif', 300, 80, 120, 3000);

-- Régime Méditerranéen
INSERT INTO diets (diet_name, carb_limit, fat_limit, protein_limit, calorie_limit)
VALUES ('Méditerranéen', 200, 80, 90, 2000);

-- Régime DASH
INSERT INTO diets (diet_name, carb_limit, fat_limit, protein_limit, calorie_limit)
VALUES ('DASH', 200, 60, 100, 2000);

-- INSERTION USERS
INSERT INTO users (name, diet_id) VALUES ('Alice Dupont', 1);
INSERT INTO users (name, diet_id) VALUES ('Bob Martin', 2);
INSERT INTO users (name, diet_id) VALUES ('Carla Durand', 3);
INSERT INTO users (name, diet_id) VALUES ('David Moreau', 4);
INSERT INTO users (name, diet_id) VALUES ('Eva Bernard', 2);
INSERT INTO users (name, diet_id) VALUES ('Franck Lambert', 1);
INSERT INTO users (name, diet_id) VALUES ('Gérard Lefèvre', 3);
INSERT INTO users (name, diet_id) VALUES ('Hélène Rousseau', 4);
INSERT INTO users (name, diet_id) VALUES ('Isabelle Petit', 5);
INSERT INTO users (name, diet_id) VALUES ('Jacques Faure', 1);



