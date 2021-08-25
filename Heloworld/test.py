import pymysql
pymysql.install_as_MySQLdb()
def divcheck(a,b):
    try:
        return a/b
    except:
        print ("Zero division error")

print (divcheck(1,0))
print ("End of prog")


