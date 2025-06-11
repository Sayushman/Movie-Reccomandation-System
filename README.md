
🎬 Movie Recommendation System

This project is a Movie Recommendation System built with Python and Streamlit for an interactive UI. It recommends movies to users based on content-based filtering (using cast, crew, genres, and keywords) and/or collaborative filtering (based on user similarity).

📌 Features
✅ Recommend similar movies based on your preferences

🎭 Uses movie metadata like cast, crew, genres, and overviews

👥 Optionally leverages collaborative filtering using user behavior

💡 Clean and minimal Streamlit UI

📊 Backend powered by pandas, scikit-learn, and optional surprise/lightfm for collaborative filtering

🧠 How It Works

📚 Content-Based Filtering:
Computes TF-IDF vectors from movie descriptions, genres, and keywords

Uses cosine similarity to find and rank similar movies

👥 Collaborative Filtering (Optional):
Uses user ratings matrix to recommend what similar users liked



🚀 Getting Started
1️⃣ Clone the Repository

git clone https://github.com/yourusername/movie-recommendation-system.git

  cd movie-recommendation-system

2️⃣ Install Requirements

  pip install -r requirements.txt

3️⃣ Run the Streamlit App

  streamlit run app.py



