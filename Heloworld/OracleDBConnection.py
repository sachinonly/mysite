# Script to Connect to Oracle Database for Python ( Valid for Oracle 11 Version with additional client install Oracle net
# For Error Cannot locate a 64-bit Oracle Client library download below according to you system Windows 32 or 64 bit or other system
# download client https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html
import cx_Oracle
import sys
import os

try:
    if sys.platform.startswith("darwin"):
        lib_dir = os.path.join(os.environ.get("HOME"), "Downloads",
                               "instantclient_19_8")
        cx_Oracle.init_oracle_client(lib_dir=lib_dir)
    elif sys.platform.startswith("win32"):
        print("You are on win32 platform !")
        lib_dir=r"C:\oraclexe\instantclient_19_11"
        cx_Oracle.init_oracle_client(lib_dir=lib_dir)
        v_tag = " Tag_Connect "
        con = cx_Oracle.connect("CDI", "CDI", "localhost/xe")
        print("Connected!")
        v_tag = " Tag_execute "
        cursor = con.cursor()
        query = cursor.execute(" select * from CUSTOMER ")
        results = cursor.fetchall()
        v_tag = " Tag_results "
        if results:
            for result in results:
                print(result)
            print("Results  Completed")
        else:
            print("No Word found")
        con.close()
except Exception as err:
    print("Error Occured at step : % s" % v_tag)
    print(err);
    sys.exit(1);