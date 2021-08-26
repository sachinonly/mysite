#pip install psycopg2

from sqlalchemy import create_engine

db_string = "postgresql://uyjudlltvcnbtw:d48e39a51a92d29c471d836a28ea1965817b6a8c61c8adab10f643259912e157@ec2-44-197-40-76.compute-1.amazonaws.com:5432/d1p9tjvu7fud3p"
db = create_engine(db_string)
# Create
#db.execute("CREATE TABLE IF NOT EXISTS users (first_name text, last_name text, company text)")
#db.execute("INSERT INTO users (first_name, last_name, company) VALUES ('Sam', 'Pitcher', 'Looker')")
# Read
result_set = db.execute("SELECT * FROM BLOOD_MASTER")
for r in result_set:
    print(r)