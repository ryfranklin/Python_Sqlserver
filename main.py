import os
from dotenv import load_dotenv
from os.path import join, dirname
import pyodbc

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

server = os.environ.get("SERVER")
username = os.environ.get("USER_NAME")
password = os.environ.get("PASSWORD")
database = os.environ.get("DATABASE")

conn = pyodbc.connect(
        '''
        Driver={ODBC DRIVER 17 for SQL server};
        SERVER=%s;
        DATABASE=%s;
        UID=%s;
        PWD=%s;
        TrustServerCertificate=yes;
        Encrypt=yes;
        ''' % (server, database, username, password)
)


cursor = conn.cursor()
cursor.execute('SELECT TOP 100 * FROM ContestPrize ')
row = cursor.fetchone()

print(row)