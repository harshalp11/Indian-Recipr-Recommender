# recipe_gui.py
import os
import pandas as pd
import numpy as np
import re
import tkinter as tk
from tkinter import messagebox
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "IndianFoodDatasetCSV.csv")

df = pd.read_csv(DATASET_PATH, engine='python')
df.columns = df.columns.str.lower().str.replace(" ", "_")
if 'recipename' in df.columns:
    df.rename(columns={'recipename': 'recipe_name'}, inplace=True)
df = df[['recipe_name', 'ingredients']].dropna()

def clean_text(t):
    t = str(t).lower()
    t = re.sub(r"[^a-zA-Z, ]", " ", t)
    return t

df['ingredients_clean'] = df['ingredients'].apply(clean_text)

nutrition_data = {
    "paneer": 265, "tomato": 18, "butter": 717, "chili": 40, "cream": 340,
    "potato": 87, "cauliflower": 25, "turmeric": 312, "onion": 40,
    "chicken": 215, "garlic": 149
}

def calculate_calories(text):
    words = [w.strip() for w in text.split(",")]
    cals = [nutrition_data.get(w) for w in words if w in nutrition_data]
    return f"{round(np.mean(cals),1)} kcal" if cals else "Unknown"

df['calories'] = df['ingredients_clean'].apply(calculate_calories)

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['ingredients_clean'])

def recommend(user_input, top_k=5):
    user_input = clean_text(user_input)
    vec = vectorizer.transform([user_input])
    sims = cosine_similarity(vec, tfidf_matrix).flatten()
    idx = sims.argsort()[::-1][:top_k]
    return [{
        "recipe_name": df.iloc[i]['recipe_name'],
        "ingredients": df.iloc[i]['ingredients'],
        "calories": df.iloc[i]['calories'],
        "similarity": float(round(sims[i],3))
    } for i in idx]

def build_gui():
    root = tk.Tk()
    root.title("Recipe Recommender")
    root.geometry("800x600")

    entry = tk.Entry(root, font=("Arial",14), width=50)
    entry.pack(pady=10)

    output = tk.Text(root, font=("Arial",12), width=90, height=25)
    output.pack()

    def find():
        text = entry.get().strip()
        if not text:
            messagebox.showwarning("Warning", "Enter ingredients")
            return
        res = recommend(text)
        output.delete("1.0", tk.END)
        for r in res:
            output.insert(tk.END, f"{r['recipe_name']}\nIngredients: {r['ingredients']}\nCalories: {r['calories']}\nSimilarity: {r['similarity']}\n{'-'*60}\n")

    btn = tk.Button(root, text="Find Recipes", command=find, font=("Arial",14))
    btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    build_gui()
