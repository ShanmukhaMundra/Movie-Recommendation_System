# 🎬🍿 Movie Recommender System

Welcome to the **Movie Recommender System**! This web app suggests movies similar to the one you select, using `content-based` filtering powered by cosine similarity. It’s built with **Python**, **Streamlit**, and preprocessed data stored in pickle files.

## 📸 Web Browser Preview
![Movie Recommender Screenshot](https://github.com/ShanmukhaMundra/Movie-Recommendation_System/blob/main/Screenshot1.png?raw=true)
---

## 📌 Features

- 🔍 Search or select any movie from the database
- 🎯 Get personalized recommendations based on similarity
- 🖼️ View posters for each recommended movie
- 🧠 Fast and lightweight with pre-computed similarity matrix

---

## 🛠️ Tech Stack

- `Python`
- `Streamlit`
- `Pandas, Scikit-learn`
- `Pickle (for data serialization)`
- `TMDb API (for movie posters)`

---

## 🗂️ Project Structure
```
├── app.py   
├── .gitattributes
├── setup.py                  
├── binary
│ ├── movie_list.pkl           
│ └── similarity1.pkl          
├── recommendation_system.ipynb 
├── requirements.txt           
├── data
│    ├──tmdb_500_credits.csv   
│    └──tmdb_500_movies.csv                
├── Screenshot.png
├── Screenshot1.png            
└── README.md
```

## 📦 Installation

**1. Clone the repository:**
```bash
git clone https://github.com/ShanmukhaMundra/Movie-Recommendation_System.git
cd Movie-Recommendation_System
```
**2. Create a virtual environment:**

*MacOS/Linux*
```bash
python -m venv venv
source venv/bin/activate
```
*Windows*
```bash
python3 -m venv venv
source venv\Scripts\activate
```
**3. Install dependencies:**

```bash
pip install -r requirements.txt
```
## 🎯 Usage
Run the Streamlit app locally:

```bash
streamlit run app.py
```
or
```
python3 -m streamlit run app.py
```

## 📸 Web Browser Output
![Movie Recommender Screenshot](https://github.com/ShanmukhaMundra/Movie-Recommendation_System/blob/main/Screenshot.png?raw=true)

## 📬 Contact
Author: `Shanmukha Mundra`   
GitHub: **@ShanmukhaMundra**
