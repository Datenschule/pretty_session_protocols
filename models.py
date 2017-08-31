import itertools
from app import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Utterance(db.Model):
    __tablename__ = "de_bundestag_plpr"

    id = db.Column(db.Integer, primary_key=True)
    wahlperiode = db.Column(db.Integer)
    sitzung = db.Column(db.Integer)
    sequence = db.Column(db.Integer)
    speaker_cleaned = db.Column(db.String)
    speaker_party = db.Column(db.String)
    speaker = db.Column(db.String)
    speaker_fp = db.Column(db.String)
    speaker_id = db.Column(db.String)
    type = db.Column(db.String)
    text = db.Column(db.String)
    top_id = db.Column(db.Integer)
    #top = relationship("Top")
    speaker_key = db.Column(db.Integer)

    @staticmethod
    def get_all(wahlperiode, session):
        return db.session.query(Utterance)\
                         .filter(Utterance.sitzung == session) \
                         .filter(Utterance.wahlperiode == wahlperiode) \
                         .order_by(Utterance.sequence) \
                         .all()

    def __repr__(self):
        return '<Utterance {}-{}-{}>'.format(self.wahlperiode, self.sitzung, self.sequence)

class MdB(db.Model):
    __tablename__ = "mdb"

    id = db.Column(db.Integer, primary_key=True)
    agw_id = db.Column(db.String)
    profile_url = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    gender = db.Column(db.String)
    birth_date = db.Column(db.Date)
    education = db.Column(db.String)
    picture = db.Column(db.String)
    party = db.Column(db.String)
    election_list = db.Column(db.String)
    list_won = db.Column(db.String)
    top_id = db.Column(db.Integer)
    education_category = db.Column(db.String)

    @staticmethod
    def get_all():
        return db.session.query(Mdb) \
            .all()

    def __repr__(self):
        return '<MdB {}-{}-{}>'.format(self.first_name, self.last_name, self.party)


class Top(db.Model):
    __tablename__ = "tops"

    id = db.Column(db.Integer, primary_key=True)
    wahlperiode = db.Column(db.Integer)
    sitzung = db.Column(db.Integer)
    title = db.Column(db.String)
    title_clean = db.Column(db.String)
    description = db.Column(db.String)
    number = db.Column(db.String)
    week = db.Column(db.Integer)
    detail = db.Column(db.String)
    year = db.Column(db.Integer)
    category = db.Column(db.String)
    duration = db.Column(db.Integer)
    held_on = db.Column(db.Date)


    @staticmethod
    def get_all():
        data = db.session.query(Top).all()

        results = []
        for key, igroup in itertools.groupby(data, lambda x: (x.wahlperiode, x.sitzung)):
            wahlperiode, sitzung = key
            results.append({"session": {"wahlperiode": wahlperiode,
                                        "sitzung": sitzung},
                            "tops": [entry.title for entry in list(igroup)]})

        return sorted(results, key=lambda entry: (entry["session"]["wahlperiode"], entry["session"]["sitzung"]))
