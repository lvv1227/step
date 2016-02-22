import socket
import thread
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',2222))
s.listen(10)
over=False

def clientthread(conn):


    while True:
        data=conn.recv(1024)
        #print("received",data)
        if not data: break
        if data.find('close')!=-1:
            conn.close()
            s.close()
            over=True
            #print("close")
            break;
        conn.send(data)
    conn.close()

while not over:

    conn, addr = s.accept()
    #print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    thread.start_new_thread(clientthread ,(conn,))

s.close()