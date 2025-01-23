from flask import Flask, request, jsonify
from models.MovieModel import Movie
from config import db
from flask_jwt_extended import jwt_required


app = Flask(__name__)

@jwt_required()
# GET all movies
def get_movies():
    movies = Movie.query.all()
    movies_list = []
    for movie in movies:
        movies_list.append(
            {
                "movie_id": movie.movie_id,
                "title": movie.title,
                "genre": movie.genre,
                "duration": movie.duration,
                "rating": movie.rating,
            }
        )
    response = {
        "status": "success",
        "data": {"movies": movies_list},
        "message": "Movies retrieved successfully",
    }
    return jsonify(response), 200

# GET a specific movie by movie_id
def get_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if not movie:
        return jsonify({"error": "error", "message": "Movie not found"}), 404

    movie_data = {
        "movie_id": movie.movie_id,
        "title": movie.title,
        "genre": movie.genre,
        "duration": movie.duration,
        "rating": movie.rating,
    }

    response = {
        "status": "success",
        "data": {"movie": movie_data},
        "message": "Movie retrieved successfully!",
    }
    return jsonify(response), 200

# POST a new movie
def add_movie():
    new_movie_data = request.get_json()
    new_movie = Movie(
        title=new_movie_data["title"],
        genre=new_movie_data["genre"],
        duration=new_movie_data["duration"],
        rating=new_movie_data["rating"],
    )
    db.session.add(new_movie)
    db.session.commit()
    return (
        jsonify({"message": "Movie added successfully!", "movie": new_movie.to_dict()}),
        201,
    )

# PUT to update an existing movie
def update_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404

    updated_data = request.get_json()
    movie.title = updated_data.get("title", movie.title)
    movie.genre = updated_data.get("genre", movie.genre)
    movie.duration = updated_data.get("duration", movie.duration)
    movie.rating = updated_data.get("rating", movie.rating)

    db.session.commit()
    return jsonify({"message": "Movie updated successfully!", "movie": movie.to_dict()})

# PATCH to partially update an existing movie
def patch_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404

    patch_data = request.get_json()
    if "title" in patch_data:
        movie.title = patch_data["title"]
    if "genre" in patch_data:
        movie.genre = patch_data["genre"]
    if "duration" in patch_data:
        movie.duration = patch_data["duration"]
    if "rating" in patch_data:
        movie.rating = patch_data["rating"]

    db.session.commit()
    return jsonify({"message": "Movie partially updated successfully!", "movie": movie.to_dict()})

# DELETE an existing movie
def delete_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404

    db.session.delete(movie)
    db.session.commit()
    return jsonify({"message": "Movie deleted successfully!"})
