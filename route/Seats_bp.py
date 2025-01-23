from flask import Blueprint
from controller.Seats_controller import get_seats, get_seat, add_seat, update_seat, delete_seat

# Seat Blueprint
seat_bp = Blueprint('seat_bp', __name__)

# Get all seats
seat_bp.route('/api/seats', methods=['GET'])(get_seats)

# Get seat by ID
seat_bp.route('/api/seats/<int:seat_id>', methods=['GET'])(get_seat)

# Add new seat
seat_bp.route('/api/seats', methods=['POST'])(add_seat)

# Update seat
seat_bp.route('/api/seats/<int:seat_id>', methods=['PUT'])(update_seat)

# Delete seat
seat_bp.route('/api/seats/<int:seat_id>', methods=['DELETE'])(delete_seat)
