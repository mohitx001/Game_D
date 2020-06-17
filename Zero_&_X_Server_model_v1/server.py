import socket

sock= socket.socket()
HOST = '127.0.0.1'
PORT=65432

sock.bind((HOST,PORT))
sock.listen(2)
print("Waiting For 2 Connection....")
conn, addr=sock.accept()
print("Client one Has connected ")
#conn.send("Welcome to in My_Game Client_1".encode())
print("Client_1 connected")
print("waiting for 1 Concection... ")
conn1, addr1=sock.accept()
print("Client_2 connected")
#conn1.send("Welcome to in My_Game Client_2".encode())

while True:
    data = conn.recv(1024).decode()  # receive data from the client, it is a blocking method
    #data = data.split('-')
    conn1.send(data)
    print(data)
    data1= conn1.recv(1024).decode()
    #data1 =data1.split('-')
    conn.send(data1)
    print(data1)