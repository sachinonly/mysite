import snowflake.connector
import pandas
print("Script to  insert test data into snowflake table from python ....")
print("Starting")

cnn1 = snowflake.connector.connect(
    user='practice',
    password='Practice123#',
    account='za80685.ap-south-1.aws',
    database='MYDB_PRACTICE',
    schema='MYDB_PRACTICE_SCHEMA'
)

print("Connecting to snowflake ..")
df1=pandas.read_csv("C:\\Personals\\Learnings\\Python\\mysite\\Heloworld\\files\\supermarkets\\testdata.csv")
cs = cnn1.cursor()
print ('Executing ...')
for i,columns in   df1.iterrows():
    print(i,columns[0],columns[1])
    cs.execute("INSERT INTO testdata VALUES (%s, %s, %s)", (columns[0], columns[1], columns[2]))
cnn1.close()



