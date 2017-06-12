from flask import Flask, render_template
import sqlite3
import os
app = Flask(__name__)

@app.route("/session/<session>")
def protocol(session):
    conn = sqlite3.connect(os.environ.get("DB_URL"))

    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    data = c.execute('select sequence, speaker_cleaned, speaker_party, type, text from de_bundestag_plpr where sitzung=?;', [session])
    return render_template('protocol.html', data=data)

if __name__ == "__main__":
    app.debug = True
    app.run()