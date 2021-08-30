#pip install --upgrade snowflake-sqlalchemy
import os
import pandas as pd
import sqlalchemy
import snowflake.connector
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL

def createtables():
    df1=pd.read_csv("C:\\Personals\\Learnings\\Python\\mysite\\Heloworld\\files\\fileslist.txt", sep =";")
    cs = conn.cursor()
    file_dir= 'C:\\Personals\\Learnings\\Python\\mysite\\Heloworld\\files'
    fileformat= 'csv'
    # Create CSV File format
    print ('*** File Format : Create ' + fileformat + " file format mycsvformat")
    cs.execute("create or replace file format mycsvformat type = " + fileformat + " field_delimiter = ',' skip_header = 1")

    # Create Internal Stage and Load the data into Table from files
    for i,columns in df1.iterrows():
        print ('Executing ...')
        filename = columns[0].upper()
        filepath = file_dir+'\\'+filename
        print("filepath: ", filepath, ",", "TableName:", columns[0] )


        print ('*** Stage Creation : Create Internal Stage:',  filename + "_INT_STAGE" )
        cs.execute("create or replace stage " + filename + '_INT_STAGE' + " file_format = mycsvformat")

        print ('*** Table Creation : Create Table :',  filename  )
        cs.execute("CREATE TABLE " + filename + ' (' + columns[1] + ' )'+ " IF NOT EXISTS" )

        print ('*** Stage Loading (put) : Create Internal Stage:',  filename + "_INT_STAGE" )
        print("put file://" + filepath + '.' + fileformat + '  @' + filename + "_INT_STAGE" + " auto_compress=true" )
        cs.execute("put file://" + filepath + '.' + fileformat + '  @' + filename + "_INT_STAGE" + " auto_compress=true" )

        print ('*** Table Load (Copy INTO) : ',columns[0] + ' from ' + columns[0] + "_INT_STAGE" )
        cs.execute("copy into "+ filename + " from @" +   filename+'_INT_STAGE/' + filename+'.csv.gz ' + " file_format = (format_name = mycsvformat error_on_column_count_mismatch=false)  " )
    conn.close()


conn = snowflake.connector.connect(
    user='practice',
    password='Practice123#',
    account='za80685.ap-south-1.aws',
    database='MYDB_PRACTICE',
    schema='MYDB_PRACTICE_SCHEMA'
)

createtables()