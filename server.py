import socket
s=socket.socket()
host=socket.gethostname()
port=9999
s.bind((host,port))
s.listen()
print("Listening...")
print("Enter this code in client machine :",host)
conn,addr=s.accept()
while True:
    data=conn.recv(1024).decode()
    if data == "quit" or data =="QUIt" or not data:
        print("Quitting")
        conn.close()
        s.close()
        break
    print("Client : ",data)
    x=input("Server : ")
    if x =="quit" or not x:
        print("Quitting")
        conn.close()
        s.close()
        break
    conn.sendall(x.encode())
