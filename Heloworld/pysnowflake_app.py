#pipenv install flask
#pipenv install flask-sqlalchemy
#pip install psycopg2 (for postgress)
#pip install mysql-connector-python (for mysql)
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sendmail import send_mail
import mysql

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Mysql123#@localhost/blooddonation'
        #'postgresql://postgres:123456@localhost/blooddonation'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://uyjudlltvcnbtw:d48e39a51a92d29c471d836a28ea1965817b6a8c61c8adab10f643259912e157@ec2-44-197-40-76.compute-1.amazonaws.com:5432/d1p9tjvu7fud3p'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#DonorName,Bloodgroup,Age,Diabetic,Weight,Comment,AadharID,MobileContact,Emailid,City,State,LastDonated
class Feedback(db.Model):
    __tablename__ = 'blood_master'
    id = db.Column(db.Integer, primary_key=True)
    DonorName = db.Column(db.String(200), unique=True)
    Bloodgroup = db.Column(db.String(200), unique=True)
    MobileContact = db.Column(db.BigInteger())
    City = db.Column(db.String(100))
    #Diabetic = db.Column(db.String(100))
    Comments = db.Column(db.Text())
    # Age = db.Column(db.Integer)
    #
    # Weight = db.Column(db.Integer)
    # Comment = db.Column(db.Text())
    # AadharID = db.Column(db.Integer())
    # MobileContact = db.Column(db.Integer())
    # Emailid = db.Column(db.Integer())
    # City = db.Column(db.String(100))
    # State = db.Column(db.String(20))
    # LastDonated = db.Column(db.String())

    #def __init__(self, id,DonorName,Bloodgroup,Age,Diabetic,Weight,Comment,AadharID,MobileContact,Emailid,City,State,LastDonated):
    #def __init__(self,DonorName,Bloodgroup,MobileContact,City,Diabetic,Comments):
    def __init__(self,DonorName,Bloodgroup,MobileContact,City,Comments):
        self.DonorName = DonorName
        self.Bloodgroup = Bloodgroup
        self.MobileContact = MobileContact
        self.City = City
        #self.Diabetic = Diabetic
        self.Comments = Comments
        # self.Age = Age
        #
        # self.Weight = Weight
        # self.AadharID = AadharID
        # self.Emailid = Emailid
        # self.State = State
        # self.LastDonated = LastDonated

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        DonorName = request.form['DonorName']
        Bloodgroup = request.form['Bloodgroup']
        MobileContact = request.form['MobileContact']
        City = request.form['City']
        #Diabetic = request.form['Diabetic']
        Comments = request.form['Comments']
        # Age = request.form['Age']
        # Weight = request.form['Weight']
        # AadharID = request.form['AadharID']
        # Emailid = request.form['Emailid']
        # State = request.form['State']
        # LastDonated = request.form['LastDonated']
        # print(customer, dealer, rating, comments)
        if DonorName == '' or Bloodgroup == '' or MobileContact == '' :
            return render_template('index.html', message='Please enter required fields')
        if db.session.query(Feedback).filter(Feedback.DonorName == DonorName).count() == 0:
            #data = Feedback(DonorName,Bloodgroup,Age,Diabetic,Weight,Comment,AadharID,MobileContact,Emailid,City,State,LastDonated)
            #data = Feedback(DonorName,Bloodgroup,MobileContact,City,Diabetic,Comments)
            data = Feedback(DonorName,Bloodgroup,MobileContact,City,Comments)
            db.session.add(data)
            db.session.commit()
            #send_mail(DonorName,Bloodgroup,MobileContact,City,Diabetic,Comments)
            #send_mail(DonorName,Bloodgroup,MobileContact,City,Comments)
            return render_template('success.html')
        return render_template('index.html', message='Thanks , You have already submitted blood details . Have a nice day ')


if __name__ == '__main__':
    app.run()