from flask import Blueprint
from controller.Booking_controller import get_bookings, get_booking, add_booking, update_booking, delete_booking

# Booking Blueprint
booking_bp = Blueprint('booking_bp', __name__)

# Get all bookings
booking_bp.route('/api/bookings', methods=['GET'])(get_bookings)

# Get booking by ID
booking_bp.route('/api/bookings/<int:booking_id>', methods=['GET'])(get_booking)

# Add new booking
booking_bp.route('/api/bookings', methods=['POST'])(add_booking)

# Update booking
booking_bp.route('/api/bookings/<int:booking_id>', methods=['PUT'])(update_booking)

# Delete booking
booking_bp.route('/api/bookings/<int:booking_id>', methods=['DELETE'])(delete_booking)