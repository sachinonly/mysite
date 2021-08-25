import snowflake.connector


print("Script to  insert data into snowflake table from python ....")
print("Starting")
snowflake.connector.paramstyle = 'qmark'

cnn = snowflake.connector.connect(
    user='practice',
    password='Practice123#',
    account='za80685.ap-south-1.aws',
    database='MYDB_PRACTICE',
    schema='MYDB_PRACTICE_SCHEMA'
)


print("Connecting to snowflake ..")
sql = ("insert into PYTHON_SNOWFLAKE_TBL "
       "(SOURCE,"
       "DESTINATION,"
       "LIBRARIES,"
       "PSEUDOCODE,"
       "PYTHONREPOSITORY,"
       "SNOWFLAKEACCOUNT,"
       "SNOWFLAKEDB)"
       " values (?,?,?,?,?,?,?);")
params = [['PythonIntelligJ','PythonSrc2','SnowflakeTGT2',
           'snowflake-connector-python  and import snowflake.connector',
           'Heloworld',
           'za80685.ap-south-1.aws',
           'MYDB_PRACTICE']]

cs = cnn.cursor()
print ('Executing ...')
cs.executemany(sql,params)
cnn.close()
