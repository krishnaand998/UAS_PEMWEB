from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS

#init db connect
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ""}}, supports_credentials=True)

app.config['JWT_SECRET_KEY'] = ''

app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()