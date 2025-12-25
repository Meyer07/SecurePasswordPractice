import sqlite3
import hashlib



connect=sqlite3.connect("userdata.db")

cursor=connect.cursor()


cursor.execute("""               
CREATE TABLE IF NOT EXISTS userdata(
        id INTEGER PRIMARY KEY,
        username VAR CHAR(255) NOT NULL,
        password VAR CHAR(255) NOT NULL
)             
""")


username1, password1= "Sam123", hashlib.sha256("sampassword".encode()).hexdigest()


print(username1)
print(password1)



