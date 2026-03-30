import unittest
import mysql.connector

def get_connection():
    return mysql.connector.connect(
    host='mysql',
    user='user',
    password='12345',
    database='cursovoi'
)

def search(tovar_id=None,name=None,price=None):
    with get_connection() as conn:
        cursor=conn.cursor()
        if tovar_id is not None and price is None and name is None:
            try:
                tovar_id=int(tovar_id)
            except ValueError as e:
                print("Ошибка в товар айди")
            cursor.execute("select * from products where id=%s",(tovar_id,))
            tovar=cursor.fetchone()
            if tovar:
                return True
            else:
                return False
        elif name is not None and price is not None and tovar_id is None:
            cursor.execute("select * from products where name=%s and price=%s",(name,price))
            tovar=cursor.fetchone()
            if tovar:
                return True
            else:
                return False
        elif name is not None and price is not None and tovar_id is not None:
            cursor.execute("select * from products where id=%s and name=%s and price=%s",(tovar_id,name,price))
            tovar=cursor.fetchone()
            if tovar:
                return True
            else:
                return False
        
        
class Testsearch(unittest.TestCase):
    def test_check_search1(self):
        self.assertTrue(search(name="ret",price=435))
    def test_check_search2(self):
        self.assertFalse(search(name="try",price=232))
    def test_check_search3(self):
        self.assertTrue(search(tovar_id=1))
    def test_check_search4(self):
        self.assertTrue(search(tovar_id=2,name="ret",price=435))
    def test_check_search5(self):
        self.assertFalse(search(tovar_id=3,name="ret",price=435))
    
if __name__=="__main__":
    unittest.main()