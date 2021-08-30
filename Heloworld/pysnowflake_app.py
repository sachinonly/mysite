#pipenv install flask
#pipenv install flask-sqlalchemy
#pip install psycopg2 (for postgress)
#pip install mysql-connector-python (for mysql)
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
#from sendmail import send_mail
import mysql
import snowflake.connector
import pandas


pysnowflake_app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    pysnowflake_app.debug = True
    pysnowflake_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Mysql123#@localhost/blooddonation'
    #'postgresql://postgres:123456@localhost/blooddonation'
    pysnowflake_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
else:
    pysnowflake_app.debug = False
    pysnowflake_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://uyjudlltvcnbtw:d48e39a51a92d29c471d836a28ea1965817b6a8c61c8adab10f643259912e157@ec2-44-197-40-76.compute-1.amazonaws.com:5432/d1p9tjvu7fud3p'

pysnowflake_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(pysnowflake_app)

def __init__(self,user,password,account,City,Comments):
        self.user = user
        self.password = password
        self.account = account


@pysnowflake_app.route('/')
def index():
    return render_template('index_pysnowflake.html')


@pysnowflake_app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        account = request.form['account']
        database = request.form['database']
        schema = request.form['schema']
        print("Checking the parameters for  Connecting to snowflake ..")
        if user == '' or password == '' or account == ''   or database == ''  or schema == '' :
            print("Connecting to snowflake ..")
        else :
            print("Connecting to snowflake .., user:",user, " account: ", account , "database: ", database, " schema: ",schema)
            cnn1 = snowflake.connector.connect(
                 user=user,
                 password=password,
                 account=account,
                 database=database,
                 schema=schema
                 )
            cs = cnn1.cursor()
            print("Connected to snowflake ..")
            print ('Executing ...')
            df1=pandas.read_csv("C:\\Personals\\Learnings\\Python\\mysite\\Heloworld\\files\\supermarkets\\testdata.csv")
            for i,columns in   df1.iterrows():
                print(i,columns[0],columns[1])
                cs.execute("INSERT INTO testdata VALUES (%s, %s, %s)", (columns[0], columns[1], columns[2]))
            cnn1.close()
            return render_template('success_pysnowflake.html', my_string="https://" + account+'.snowflakecomputing.com', my_list=["USER: "+ user, "ACCOUNT: "+ account, "DATABASE: "+ database,"SCHEMA: "+ schema])
        #return render_template('index_pysnowflake.html', message='Error .. check input, Try again ',)


if __name__ == '__main__':
    pysnowflake_app.run()