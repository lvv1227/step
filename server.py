import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',2222))
s.listen(10)
over=False
while not over:
    conn,addr=s.accept()
    while True:
        data=conn.recv(1024)
        #print("received",data)
        if not data: break
        if data == 'close':
            conn.close()
            s.close()
            over=True
            #print("close")
            break;
        conn.send(data)
    conn.close()