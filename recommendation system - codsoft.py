import numpy as np

# Sample movie data (movie genres)
movies_data = {
    'Inception': np.array([1, 0, 1, 0, 0]),       # Action, Sci-Fi
    'The Hangover': np.array([1, 1, 0, 0, 1]),    # Action, Comedy, Romance
    'Interstellar': np.array([0, 0, 1, 0, 0]),    # Sci-Fi
    'The Notebook': np.array([0, 0, 0, 1, 1]),    # Drama, Romance
    'The Dark Knight': np.array([1, 0, 0, 1, 0])  # Action, Drama
}

def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    magnitude = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    if magnitude == 0:
        return 0
    return dot_product / magnitude

def get_user_preferences():
    print("Welcome to the Movie Recommendation System!")
    print("Please enter your preferred movie genres:")
    print("Genres: Action, Comedy, Sci-Fi, Drama, Romance")
    preferences = np.zeros(5)  # Initialize preferences array
    genres = ["Action", "Comedy", "Sci-Fi", "Drama", "Romance"]
    for i, genre in enumerate(genres):
        choice = input(f"Do you like {genre}? (yes/no): ").lower()
        if choice == 'yes':
            preferences[i] = 1
    return preferences

def recommend_movies(movies_data, user_preferences, n=3):
    # Calculate cosine similarity between user preferences and movie genres for each movie
    similarities = {}
    for movie, features in movies_data.items():
        similarities[movie] = cosine_similarity(user_preferences, features)
    
    # Sort movies by similarity in descending order
    sorted_movies = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
    
    # Return top N recommended movies based on similarity
    recommended_movies = sorted_movies[:n]
    return recommended_movies

# Get user preferences
user_preferences = get_user_preferences()

# Get recommended movies for the user
recommended_movies = recommend_movies(movies_data, user_preferences, n=3)

# Print the recommended movies with real movie names
movie_names = {
    'Inception': 'Inception',
    'The Hangover': 'The Hangover',
    'Interstellar': 'Interstellar',
    'The Notebook': 'The Notebook',
    'The Dark Knight': 'The Dark Knight'
}

print("\nRecommended movies:")
for movie, similarity in recommended_movies:
    print(f"{movie_names[movie]} (Similarity: {similarity:.2f})")
