from flask import Flask, request, jsonify
from models.SeatsModel import Seat
from models.UserModel import User
from models.JadwalModel import Schedule
from config import db
from flask_jwt_extended import jwt_required

app = Flask(__name__)

@jwt_required()
# GET all seats
def get_seats():
    seats = Seat.query.all()
    seats_list = []
    for seat in seats:
        seats_list.append(
            {
                "seat_id": seat.seat_id,
                "schedule_id": seat.schedule_id,
                "seat_number": seat.seat_number,
                "status": seat.status,
            }
        )
    response = {
        "status": "success",
        "data": {"seats": seats_list},
        "message": "Seats retrieved successfully",
    }
    return jsonify(response), 200

# GET a specific seat by seat_id
def get_seat(seat_id):
    seat = Seat.query.get(seat_id)
    if not seat:
        return jsonify({"error": "error", "message": "Seat not found"}), 404

    seat_data = {
        "seat_id": seat.seat_id,
        "schedule_id": seat.schedule_id,
        "seat_number": seat.seat_number,
        "status": seat.status,
    }

    response = {
        "status": "success",
        "data": {"seat": seat_data},
        "message": "Seat retrieved successfully!",
    }
    return jsonify(response), 200

# POST a new seat
def add_seat():
    new_seat_data = request.get_json()
    new_seat = Seat(
        schedule_id=new_seat_data["schedule_id"],
        seat_number=new_seat_data["seat_number"],
        status=new_seat_data.get("status", "available"),
    )
    db.session.add(new_seat)
    db.session.commit()
    return (
        jsonify({"message": "Seat added successfully!", "seat": new_seat.to_dict()}),
        201,
    )

# DELETE an existing seat
def delete_seat(seat_id):
    seat = Seat.query.get(seat_id)
    if not seat:
        return jsonify({"error": "Seat not found"}), 404

    db.session.delete(seat)
    db.session.commit()
    return jsonify({"message": "Seat deleted successfully!"})
