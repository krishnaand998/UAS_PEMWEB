from flask import Blueprint
from controller.Movie_controller import get_movies, get_movie, add_movie, update_movie, delete_movie

# Movie Blueprint
movie_bp = Blueprint('movie_bp', __name__)

# Get all movies
movie_bp.route('/api/movies', methods=['GET'])(get_movies)

# Get movie by ID
movie_bp.route('/api/movies/<int:movie_id>', methods=['GET'])(get_movie)

# Add new movie
movie_bp.route('/api/movies', methods=['POST'])(add_movie)

# Update movie
movie_bp.route('/api/movies/<int:movie_id>', methods=['PUT'])(update_movie)

# Delete movie
movie_bp.route('/api/movies/<int:movie_id>', methods=['DELETE'])(delete_movie)
