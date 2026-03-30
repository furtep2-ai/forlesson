import mysql.connector
import re
import unittest
def get_connection():
    return mysql.connector.connect(
    host='localhost',
    user='user',
    password='12345',
    database='cursovoi'
)
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$"

def register(name,password):
        if re.match(pattern,password):
            if re.match(pattern,name):
                with get_connection() as conn:
                    cursor=conn.cursor()
                    cursor.execute("insert into users1 (name,password) values (%s,%s)",(name,password))
                    conn.commit()
                    cursor.execute("select * from users1 where name=%s and password=%s",(name,password))
                    check=cursor.fetchone()
                    if check:
                        
                        return True
                    else:
                        
                        return False
        else:
            return False
def login(name,password):
        with get_connection() as conn:
            cursor=conn.cursor()
            cursor.execute("select * from users1 where name=%s and password=%s",(name,password))
            user=cursor.fetchone()
            if user:
                
                return True
            else:
                
                return False

class Testreg(unittest.TestCase):
    def test_register1(self):
        self.assertTrue(register("Namee24235","35352Fssg"))

    def test_register2(self):
        self.assertFalse(register("Namee24235","35352Fssg+_- "))

    def test_register3(self):
        self.assertFalse(register("Namee24235+=2--=-=--","35352Fssg"))

    def test_login1(self):
        self.assertTrue(login("New232io42","Gersolo2009"))

    def test_login2(self):
        self.assertFalse(login("ret ","Gersolo2009"))

    def test_login3(self):
        self.assertFalse(login("ret","Gersolo2009 "))

    def test_login4(self):
        self.assertFalse(login("ret+","Gersolo200923"))
        
if __name__=="__main__":
    unittest.main()