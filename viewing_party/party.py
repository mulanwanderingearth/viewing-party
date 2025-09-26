# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    if not title or not genre or not rating :
        return None 
    else:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie
    
    
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data 


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data 

def watch_movie(user_data,title):

    for movie in user_data["watchlist"] :

        if title in movie["title"] :
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0
    
    total_rating = 0.0
    for movie in user_data["watched"]:
        total_rating += movie["rating"]
    average_rating = total_rating/len(user_data["watched"])   
    return average_rating
        
def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    genre_dict = {}
    for movie in user_data["watched"]:
        genre_dict[movie["genre"]] = genre_dict.get(movie["genre"],0) + 1

    max_count = 0
    most_watched_genre = ""
    
    for genre_name, genre_count in genre_dict.items():
        if genre_count > max_count :
            max_count = genre_count
            most_watched_genre = genre_name

    return most_watched_genre        





# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

    unique_watched = []
    friends_movie_titles = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movie_titles.add(movie["title"])
    for movie in user_data["watched"]:
        if movie["title"] not in friends_movie_titles:
            unique_watched.append(movie)       
    return unique_watched 


def get_friends_unique_watched(user_data):
    # unique_movies = []
    # friends_watched_movies = []
    # for friend in user_data["friends"]:
    #     for movie in friend["watched"]:
    #         if movie not in friends_watched_movies:
    #             friends_watched_movies.append(movie)
    # for movie in friends_watched_movies:
    #     if movie not in user_data["watched"]:
    #         unique_movies.append(movie)

    # return unique_movies       

    user_watched_titles = set()
    friends_watched_titles = set()
    unique_titles = set()
    unique_movie = []

    for movie in user_data["watched"]:
        user_watched_titles.add(movie["title"])
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_titles.add(movie["title"])


    unique_titles = friends_watched_titles - user_watched_titles

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] in unique_titles and movie not in unique_movie:
                unique_movie.append(movie)

    return unique_movie

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    unique_movies = get_friends_unique_watched(user_data)
    recommended_movies =[]
    for movie in unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)

    return recommended_movies        







# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    recommendations = []
    most_watched_genre = get_most_watched_genre(user_data)
    friends_movies = get_friends_unique_watched(user_data)
    for movie in friends_movies:
        if movie["genre"] == most_watched_genre :
            recommendations.append(movie)
    return recommendations
def get_rec_from_favorites(user_data):
    unique_watched = []
    friends_movie=[]
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movie.append(movie)
    for movie in user_data["favorites"]:
        if movie not in friends_movie:
            unique_watched.append(movie)
    return unique_watched