import json
import os

from flask import render_template, request

from app import app
from models import Utterance, Top


def get_mdbs():
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, './matches.json')
    with open(filename) as infile:
        return json.load(infile)


@app.route("/session/<session>")
def protocol(session):
    data = Utterance.get_all(18, session)
    mdbs = get_mdbs()
    for utterance in data:
        utterance.agw_url = mdbs.get(utterance.speaker_fp)
    debug = request.args.get("debug")
    return render_template('protocol.html', data=data, debug=debug)


@app.route("/session/")
def protocol_overview():
    sessions = Top.get_all()
    return render_template('protocol_overview.html', sessions=sessions)


@app.route("/")
def index():
    return "Placeholder", 200


if __name__ == "__main__":
    app.debug = os.environ.get("DEBUG", False)
    app.jinja_env.auto_reload = app.debug
    app.config['TEMPLATES_AUTO_RELOAD'] = app.debug
    app.run(host="0.0.0.0")
