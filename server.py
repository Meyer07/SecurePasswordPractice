import sqlite3
import hashlib
import socket
import threading

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind("localhost",9999)

server.listen()


def handleConnection(c):
    c.send("Username: ".encode())
    username=c.recv(1024).decode()
    c.send("Password: ".encode())
    password=c.recv(1024)
    password=hashlib.sha256(password).hexdigest()

    connection=sqlite3.connect("userdata.db")
    cursor=connection.cursor()

    cursor.execute("SELECT * FROM userdata WHERE username = ? AND password=?",(username,password))

    if(cursor.fetchall()):
        c.send("Login Successful").encode()
    else:
        c.send("Login not successful").encode()


while True:
    client, address = server.accept()
    threading.thread(target=handle_connection, args=(client,)).start()