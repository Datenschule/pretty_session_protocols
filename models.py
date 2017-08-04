import itertools
from app import db


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
    top = db.Column(db.String)
    type = db.Column(db.String)
    text = db.Column(db.String)
    agw_url = None

    @staticmethod
    def get_all(wahlperiode, session):
        return db.session.query(Utterance)\
                         .filter(Utterance.sitzung == session) \
                         .filter(Utterance.wahlperiode == wahlperiode) \
                         .order_by(Utterance.sequence) \
                         .all()

    @staticmethod
    def get_sessions():
        data = db.session.query(Utterance.wahlperiode, Utterance.sitzung, Utterance.top) \
                 .distinct(Utterance.wahlperiode, Utterance.sitzung, Utterance.top) \
                 .all()

        results = []
        for key, igroup in itertools.groupby(data, lambda x: (x.wahlperiode, x.sitzung)):
            wahlperiode, sitzung = key
            results.append({"session": {"wahlperiode": wahlperiode,
                                        "sitzung": sitzung},
                            "tops": [entry.top for entry in list(igroup) if entry.top is not None]})

        return sorted(results, key=lambda entry: (entry["session"]["wahlperiode"], entry["session"]["sitzung"]))

    def __repr__(self):
        return '<Utterance {}-{}-{}>'.format(self.wahlperiode, self.sitzung, self.sequence)