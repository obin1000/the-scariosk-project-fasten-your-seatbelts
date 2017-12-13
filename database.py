#Installleer de volgende dingen:
#sudo apt install python-pip
#sudo pip3 install PyMySQL
#suco apt install mysql-server 
import pymysql
class database:

    def insertData(self, id, path):
        conn = pymysql.connect('127.0.0.1','scariosk','veryscary','scariosk')
        cur = conn.cursor()
        if conn:
            print('connection succes' + id + path)
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
            