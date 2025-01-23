from config import db

class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # Durasi dalam menit
    rating = db.Column(db.Float, nullable=False)  # Rating film

    def to_dict(self):
        return {
            'movie_id': self.movie_id,
            'title': self.title,
            'genre': self.genre,
            'duration': self.duration,
            'rating': self.rating
        }
