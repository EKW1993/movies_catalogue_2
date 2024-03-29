from flask import Flask, render_template, request, url_for

app = Flask(__name__)

import tmdb_client
import random

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', 'popular')
    valid_lists = ['popular', 'top_rated', 'upcoming', 'now_playing']
    if selected_list not in valid_lists:
        selected_list = 'popular'
    movies = tmdb_client.get_movies(list_type=selected_list)
    lists = tmdb_client.get_movies_list(list_type=selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list, lists=lists)
    
@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops'])
    return render_template("movie_details.html", movie=details, cast=cast, selected_backdrop=selected_backdrop)
