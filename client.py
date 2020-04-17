import socket
s=socket.socket()
n=input("Enter the code given from server machine : ")
host=n
port=9999
s.connect((host,port))
while True:
    x=input("Client : ")
    if x =="quit" or not x:
        print("Quitting")
        s.close()
        break
    s.sendall(x.encode())
    data=s.recv(1024).decode()
    if data =="quit" or data =="QUIT" or not data:
        print("Quitting")
        s.close()
        break
    print("Server : ",data)

