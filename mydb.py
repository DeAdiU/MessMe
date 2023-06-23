import mysql.connector
dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='adiu2004'
)


cursorobject=dataBase.cursor()

cursorobject.execute("CREATE DATABASE MessMe")
print('All done')