from flask import Blueprint
from controller.Jadwal_controller import get_schedules, get_schedule, add_schedule, update_schedule, delete_schedule

# Schedule Blueprint
schedule_bp = Blueprint('schedule_bp', __name__)

# Get all schedules
schedule_bp.route('/api/schedules', methods=['GET'])(get_schedules)

# Get schedule by ID
schedule_bp.route('/api/schedules/<int:schedule_id>', methods=['GET'])(get_schedule)

# Add new schedule
schedule_bp.route('/api/schedules', methods=['POST'])(add_schedule)

# Update schedule
schedule_bp.route('/api/schedules/<int:schedule_id>', methods=['PUT'])(update_schedule)

# Delete schedule
schedule_bp.route('/api/schedules/<int:schedule_id>', methods=['DELETE'])(delete_schedule)
