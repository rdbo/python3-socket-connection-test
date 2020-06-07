import socket
import time

host = "127.0.0.1"
port = 4444
sock = socket.socket()

#Bind Socket

try:
    sock.bind((host, port))
    sock.listen(5)

except socket.error:
    print("[*] An error occurred")
    exit(-1)

#Accept connection
conn, address = sock.accept()

while True:
    try:
        msg = str(conn.recv(256).decode())
        print("[*] Received message: " + msg)
        conn.send(str.encode("Your message has been received"))

        time.sleep(0.5)
    except:
        print()
        print("[*] Exception raised, exiting...")
        conn.close()
        sock.close()
        exit(0)