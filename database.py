#Installleer de volgende dingen:
#sudo apt install python-pip
#sudo pip3 install PyMySQL
#suco apt install mysql-server
from random import randint
import pymysql
class database:

    def insertData(self, id, path):
        conn = pymysql.connect('127.0.0.1','scariosk','veryscary','scariosk')
        cur = conn.cursor()
        if conn:
            cur.execute("INSERT INTO fotodata  (fotoid,path) VALUES (%s,%s)", (id, path))
            conn.commit()

            
    def checkCode(self, code):
        conn = pymysql.connect('127.0.0.1','scariosk','veryscary','scariosk')
        cur = conn.cursor()
        if conn:
            result = cur.execute("SELECT * FROM fotodata WHERE fotoid = (%s)", code)
            data = cur.fetchall()
                
            if not data:
                return True
            else:
                return False
            
    def generateCode(self):
        base = database()
        code = randint(111111,999999)
        while True:
            if base.checkCode(code):
                return code
                break
            else:
                code = randint(111111,999999)
            