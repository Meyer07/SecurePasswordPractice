import sqlite3
import hashlib


##connects to the userdata database as initialized below
connect=sqlite3.connect("userdata.db")

cursor=connect.cursor()

##this SQL function creates a table of keys,usernames and passwords and gives the usernames and passwords
##the ability to hold char values and restricts them from having not null values
cursor.execute("""               
CREATE TABLE IF NOT EXISTS userdata(
        id INTEGER PRIMARY KEY,
        username VAR CHAR(255) NOT NULL,
        password VAR CHAR(255) NOT NULL
)             
""")

##the hashlib import gives me access to various hashing tools including the use of the sha256 hash and being able to put 
##even simple passwords through it 
username1, password1= "Sam123", hashlib.sha256("sampassword".encode()).hexdigest()


print(username1)
print(password1)


while True:
    username=input("Please enter a username: ")
    password=input("Please enter a very secure password: ")

    if(username.isalnum() and password.isalnum()):
        break


cursor.execute("INSERT INTO userdata (username, password) VALUES(?,?)", (username,password))

connect.commit()




