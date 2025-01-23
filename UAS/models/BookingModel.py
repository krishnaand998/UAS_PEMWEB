from config import db
from datetime import datetime

class Booking(db.Model):
    __tablename__ = 'bookings'
    
    booking_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    schedule_id = db.Column(db.Integer, db.ForeignKey('schedules.schedule_id'), nullable=False)
    seat_id = db.Column(db.Integer, db.ForeignKey('seats.seat_id'), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(
        db.Enum('confirmed', 'cancelled', name='booking_status'),
        nullable=False,
        default='confirmed'
    )
    
    def to_dict(self):
        return {
            'booking_id': self.booking_id,
            'user_id': self.user_id,
            'schedule_id': self.schedule_id,
            'seat_id': self.seat_id,
            'booking_date': self.booking_date.isoformat() if self.booking_date else None,
            'status': self.status
        }
