from flask import Flask, request, jsonify
from models.UserModel import User
from models.JadwalModel import Schedule
from models.SeatsModel import Seat
from models.BookingModel import Booking
from config import db
from flask_jwt_extended import jwt_required

app = Flask(__name__)


@jwt_required()
# GET all bookings
def get_bookings():
    bookings = Booking.query.all()
    bookings_list = []
    for booking in bookings:
        bookings_list.append(
            {
                "booking_id": booking.booking_id,
                "user_id": booking.user_id,
                "schedule_id": booking.schedule_id,
                "seat_id": booking.seat_id,
                "booking_date": booking.booking_date.strftime("%Y-%m-%d %H:%M:%S"),
                "status": booking.status,
            }
        )
    response = {
        "status": "success",
        "data": {"bookings": bookings_list},
        "message": "Bookings retrieved successfully",
    }
    return jsonify(response), 200

# GET a specific booking by booking_id
def get_booking(booking_id):
    booking = Booking.query.get(booking_id)
    if not booking:
        return jsonify({"error": "error", "message": "Booking not found"}), 404

    booking_data = {
        "booking_id": booking.booking_id,
        "user_id": booking.user_id,
        "schedule_id": booking.schedule_id,
        "seat_id": booking.seat_id,
        "booking_date": booking.booking_date.strftime("%Y-%m-%d %H:%M:%S"),
        "status": booking.status,
    }

    response = {
        "status": "success",
        "data": {"booking": booking_data},
        "message": "Booking retrieved successfully!",
    }
    return jsonify(response), 200

# POST a new booking
def add_booking():
    new_booking_data = request.get_json()
    new_booking = Booking(
        user_id=new_booking_data["user_id"],
        schedule_id=new_booking_data["schedule_id"],
        seat_id=new_booking_data["seat_id"],
        booking_date=new_booking_data["booking_date"],
        status=new_booking_data.get("status", "confirmed"),
    )
    db.session.add(new_booking)
    db.session.commit()
    return (
        jsonify({"message": "Booking added successfully!", "booking": new_booking.to_dict()}),
        201,
    )

# UPDATE an existing booking
def update_booking(booking_id):
    booking = Booking.query.get(booking_id)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404

    updated_data = request.get_json()
    booking.user_id = updated_data.get("user_id", booking.user_id)
    booking.schedule_id = updated_data.get("schedule_id", booking.schedule_id)
    booking.seat_id = updated_data.get("seat_id", booking.seat_id)
    booking.booking_date = updated_data.get("booking_date", booking.booking_date)
    booking.status = updated_data.get("status", booking.status)

    db.session.commit()
    return jsonify({"message": "Booking updated successfully!", "booking": booking.to_dict()}), 200

# DELETE an existing booking
def delete_booking(booking_id):
    booking = Booking.query.get(booking_id)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404

    db.session.delete(booking)
    db.session.commit()
    return jsonify({"message": "Booking deleted successfully!"})