🍛 Indian Recipe Recommender (NLP + TF-IDF)

An Indian Recipe Recommendation System built using Natural Language Processing (NLP) and TF-IDF vectorization. The application recommends recipes based on the ingredients available with the user. Simply enter the ingredients you have, and the system suggests the most relevant Indian recipes along with their ingredient lists and estimated calories.

This project demonstrates practical implementation of text preprocessing, TF-IDF vectorization, cosine similarity, and GUI development in Python.

🚀 Features

Ingredient-based recipe recommendation

NLP text preprocessing of ingredient data

TF-IDF vectorization for ingredient representation

Cosine similarity to find the most relevant recipes

Estimated calorie information for recipes

Simple Tkinter GUI interface

Returns Top 5 matching recipes

🧠 How It Works

The dataset of Indian recipes is loaded.

Ingredient text is cleaned and normalized.

Ingredients are converted into numerical vectors using TF-IDF.

User input ingredients are vectorized.

Cosine similarity is calculated between user input and all recipes.

The system returns the most similar recipes.

🛠 Tech Stack

Python

Pandas

NumPy

Scikit-learn

Tkinter (GUI)

TF-IDF Vectorizer

Cosine Similarity

📂 Project Structure
project-folder
│
├── recipe_gui.py
├── IndianFoodDatasetCSV.csv
└── README.md

The main application logic and GUI are implemented in recipe_gui.py. 

recipe_gui

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/indian-recipe-recommender.git
cd indian-recipe-recommender
2️⃣ Install dependencies
pip install pandas numpy scikit-learn

(Tkinter usually comes preinstalled with Python.)

▶️ Running the Application

Run the Python file:

python recipe_gui.py

A GUI window will open where you can enter ingredients and get recipe recommendations.

💡 Example

Input ingredients:

tomato, onion, garlic, butter

Output:

Butter Chicken
Ingredients: chicken, butter, tomato, cream...
Calories: 340 kcal
Similarity: 0.73


📊 Future Improvements

Add larger recipe datasets

Improve nutrition calculation

Deploy as a web application (Streamlit / Flask)

Add image previews of recipes

Implement deep learning based recommendations

👨‍💻 Author

Harshal Patil
B.Tech Computer Science Engineering
