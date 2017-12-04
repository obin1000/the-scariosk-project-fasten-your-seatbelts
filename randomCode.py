from random import randint
from database import database

class randomCode:
    def generateCode(self):
        base = database()
        code = randint(111111,999999)
        while True:
            if base.checkCode(code):
                return code
                break
            else:
                code = randint(111111,999999)
        
        
