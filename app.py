from datetime import datetime
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Entry(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    prod_url = db.Column(db.String)
    wanted_price = db.Column(db.Integer)
    email_id = db.Column(db.String)
    date = db.Column(db.DateTime)

    def __init__(self, prod_url, wanted_price, email_id, date):
        self.prod_url = prod_url
        self.wanted_price = wanted_price
        self.email_id = email_id
        self.date = date

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html')
    entry = Entry(request.form['prodUrl'], request.form['wantedPrice'], request.form['mailId'], datetime.now())
    db.session.add(entry)
    db.session.commit()
    return render_template('received.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
