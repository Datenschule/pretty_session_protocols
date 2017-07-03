from flask import render_template

from app import app
from models import Utterance


@app.route("/session/<session>")
def protocol(session):
    data = Utterance.get_all(18, session)
    return render_template('protocol.html', data=data)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
