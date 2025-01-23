from config import db

class Seat(db.Model):
    __tablename__ = 'seats'
    
    seat_id = db.Column(db.Integer, primary_key=True)
    schedule_id = db.Column(db.Integer, db.ForeignKey('schedules.schedule_id'), nullable=False)
    seat_number = db.Column(db.String(10), nullable=False)
    status = db.Column(
        db.Enum('available', 'booked', name='seat_status'),
        nullable=False,
        default='available'
    )
    
    def to_dict(self):
        return {
            'seat_id': self.seat_id,
            'schedule_id': self.schedule_id,
            'seat_number': self.seat_number,
            'status': self.status
        }
