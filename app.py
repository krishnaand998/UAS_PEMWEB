from config import app, db
from route.Booking_bp import booking_bp
from route.Jadwal_bp import schedule_bp
from route.Movie_bp import movie_bp
from route.Seats_bp import seat_bp
from route.User_bp import user_bp
from flask import request, jsonify

#Inisialisasi JWTManager
jwt = JWTManager(app)

@app.route("/api/protected", methods=["GET"])
@jwt_required()
def protected():
    print("Headers Received:", request.headers)  # Debugging Header
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.before_request
def before_request():
    # Daftar endpoint yang dikecualikan dari autentikasi
    excluded_routes = ['/api/login', '/api/register']
    if request.path in excluded_routes:
        return None  # Lewati autentikasi untuk route ini
    return None

app.register_blueprint(booking_bp)
app.register_blueprint(schedule_bp)
app.register_blueprint(movie_bp)
app.register_blueprint(seat_bp)
app.register_blueprint(user_bp)



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)