from config import db
from sqlalchemy.orm import relationship

class Schedule(db.Model):
    schedule_id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.movie_id'), nullable=False)
    screen = db.Column(db.String(50), nullable=False)  # Nomor studio/layar
    showtime = db.Column(db.DateTime, nullable=False)  # Waktu penayangan

    # Relasi ke tabel Movie
    movie = relationship('Movie', backref='schedules')

    def to_dict(self):
        return {
            'schedule_id': self.schedule_id,
            'movie_id': self.movie_id,
            'screen': self.screen,
            'showtime': self.showtime.strftime('%Y-%m-%d %H:%M:%S'),  # Format datetime
            'movie_title': self.movie.title if self.movie else None
        }
