from flask import Flask, request, jsonify
from flask_jwt_extended import jwt_required
from models.UserModel import User
from config import db 

app = Flask(__name__)

# Register a new user
def register_user():
    new_user_data = request.get_json()
    if User.query.filter_by(email=new_user_data['email']).first():
        return jsonify({"error": "Email already exists"}), 400

    new_user = User(
        name=new_user_data["name"],
        email=new_user_data["email"],
        password=new_user_data["password"],
        role=new_user_data.get("role", "user")  # Default role is 'user'
    )
    db.session.add(new_user)
    db.session.commit()

    access_token = create_access_token(identity={"user_id": new_user.user_id, "role": new_user.role})
    
    return jsonify({
        "message": "User registered successfully!",
        "user": {
            "user_id": new_user.user_id,
            "name": new_user.name,
            "email": new_user.email,
            "role": new_user.role
        },
        "access_token": access_token
    }), 201

@jwt_required()
# GET all users
def get_users():
    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append(
            {
                "user_id": user.user_id,
                "name": user.name,
                "email": user.email,
                "role": user.role,
            }
        )
    response = {
        "status": "success",
        "data": {"users": users_list},
        "message": "Users retrieved successfully",
    }
    return jsonify(response), 200

# GET a specific user by user_id
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "error", "message": "User not found"}), 404

    user_data = {
        "user_id": user.user_id,
        "name": user.name,
        "email": user.email,
        "role": user.role,
    }

    response = {
        "status": "success",
        "data": {"user": user_data},
        "message": "User retrieved successfully!",
    }
    return jsonify(response), 200

# POST a new user
def add_user():
    new_user_data = request.get_json()
    new_user = User(
        name=new_user_data["name"],
        email=new_user_data["email"],
        password=new_user_data["password"],
        role=new_user_data.get("role", "user"),  # Default role is 'user'
    )
    db.session.add(new_user)
    db.session.commit()
    return (
        jsonify({"message": "User added successfully!", "user": new_user.to_dict()}),
        201,
    )

# UPDATE an existing user
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    updated_data = request.get_json()
    user.name = updated_data.get("name", user.name)
    user.email = updated_data.get("email", user.email)
    user.password = updated_data.get("password", user.password)
    user.role = updated_data.get("role", user.role)

    db.session.commit()
    return jsonify({"message": "User updated successfully!", "user": user.to_dict()})

# PATCH to partially update an existing user
def patch_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    patch_data = request.get_json()
    if "name" in patch_data:
        user.name = patch_data["name"]
    if "email" in patch_data:
        user.email = patch_data["email"]
    if "password" in patch_data:
        user.password = patch_data["password"]
    if "role" in patch_data:
        user.role = patch_data["role"]

    db.session.commit()
    return jsonify({"message": "User partially updated successfully!", "user": user.to_dict()})

# DELETE an existing user
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully!"})