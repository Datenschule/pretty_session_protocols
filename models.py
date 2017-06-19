import os

from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Utterance(db.Model):
    __tablename__ = "de_bundestag_plpr"

    id = db.Column(db.Integer, primary_key=True)
    wahlperiode = db.Column(db.Integer)
    sitzung = db.Column(db.Integer)
    sequence = db.Column(db.Integer)
    speaker_cleaned = db.Column(db.String)
    speaker_party = db.Column(db.String)
    type = db.Column(db.String)
    text = db.Column(db.String)

    @staticmethod
    def get_all(wahlperiode, session):
        return db.session.query(Utterance)\
                         .filter(Utterance.sitzung == session) \
                         .filter(Utterance.wahlperiode == wahlperiode) \
                         .order_by(Utterance.sequence) \
                         .all()

    def __repr__(self):
        return '<Utterance %r>' % self.sitzung