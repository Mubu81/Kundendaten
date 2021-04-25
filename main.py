from flask import Flask, render_template, request, url_for, redirect, make_response
from models import db, Kundendaten

app = Flask(__name__)

db.create_all()


@app.route('/')
def kunden():
    anfragen_db = db.query(Kundendaten).all()
    return render_template("kundendaten.html", anfragen=anfragen_db)


@app.route("/kundendaten", methods=["POST"])
def infos():
    vorname = request.form.get("vorname")
    nachname = request.form.get("nachname")
    strasse = request.form.get("strasse")
    hausnummer = request.form.get("hausnummer")
    plz = request.form.get("plz")
    stadt = request.form.get("stadt")
    email = request.form.get("email")
    tel = request.form.get("tel")
    new_request = Kundendaten(vorname=vorname, nachname=nachname, strasse=strasse, hausnummer=hausnummer,
                              plz=plz, stadt=stadt, email=email, tel=tel)
    db.add(new_request)
    db.commit()
    anfragen_db = db.query(Kundendaten).all()
    return redirect(url_for("kunden"))


@app.route('/delete', methods=['POST'])
def delete():
    id = request.form.get("id")
    db.query(Kundendaten).filter_by(id=id).delete()

    db.commit()
    return redirect(url_for("kunden"))


if __name__ == '__main__':
    app.run()
