from flask import Blueprint
from controller.User_controller import get_users, get_user, add_user, update_user, delete_user


# User Blueprint
user_bp = Blueprint('user_bp', __name__)

# Get all users
user_bp.route('/api/users', methods=['GET'])(get_users)

# Get user by ID
user_bp.route('/api/users/<int:user_id>', methods=['GET'])(get_user)

# Add new user
user_bp.route('/api/users', methods=['POST'])(add_user)

# Update user
user_bp.route('/api/users/<int:user_id>', methods=['PUT'])(update_user)

# Delete user
user_bp.route('/api/users/<int:user_id>', methods=['DELETE'])(delete_user)
