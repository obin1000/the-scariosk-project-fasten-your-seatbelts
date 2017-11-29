#Installleer de volgende dingen:
#sudo apt-get install python-pip
#sudo pip install PyMySQL
#sudo pip2 install PyMySQL
#sudo pip3 install PyMySQL
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
        print(code)
        if conn:
            result = cur.execute("SELECT * FROM fotodata WHERE fotoid = (%s)", code)
            conn.commit()
            if result > 0:
                return 0
            else:
                return 1
            