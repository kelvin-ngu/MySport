from flask import Flask, url_for, render_template
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///PlayerVoice.db'
db = SQLAlchemy(app)

class PlayerDB(db.models):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    age = db.Column(db.Integer, nullable = False)
    club = db.Column(db.String, nullable = False)

