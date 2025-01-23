from flask import Flask, request, jsonify
from models.UserModel import User
from models.JadwalModel import Schedule
from config import db
from flask_jwt_extended import jwt_required

app = Flask(__name__)

@jwt_required()
# GET all schedules
def get_schedules():
    schedules = Schedule.query.all()
    schedules_list = []
    for schedule in schedules:
        schedules_list.append(
            {
                "schedule_id": schedule.schedule_id,
                "movie_id": schedule.movie_id,
                "screen": schedule.screen,
                "showtime": schedule.showtime.strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
    response = {
        "status": "success",
        "data": {"schedules": schedules_list},
        "message": "Schedules retrieved successfully",
    }
    return jsonify(response), 200

# GET a specific schedule by schedule_id
def get_schedule(schedule_id):
    schedule = Schedule.query.get(schedule_id)
    if not schedule:
        return jsonify({"error": "error", "message": "Schedule not found"}), 404

    schedule_data = {
        "schedule_id": schedule.schedule_id,
        "movie_id": schedule.movie_id,
        "screen": schedule.screen,
        "showtime": schedule.showtime.strftime("%Y-%m-%d %H:%M:%S"),
    }

    response = {
        "status": "success",
        "data": {"schedule": schedule_data},
        "message": "Schedule retrieved successfully!",
    }
    return jsonify(response), 200

# POST a new schedule
def add_schedule():
    new_schedule_data = request.get_json()
    new_schedule = Schedule(
        movie_id=new_schedule_data["movie_id"],
        screen=new_schedule_data["screen"],
        showtime=new_schedule_data["showtime"],
    )
    db.session.add(new_schedule)
    db.session.commit()
    return (
        jsonify({"message": "Schedule added successfully!", "schedule": new_schedule.to_dict()}),
        201,
    )

# DELETE an existing schedule
def delete_schedule(schedule_id):
    schedule = Schedule.query.get(schedule_id)
    if not schedule:
        return jsonify({"error": "Schedule not found"}), 404

    db.session.delete(schedule)
    db.session.commit()
    return jsonify({"message": "Schedule deleted successfully!"})
