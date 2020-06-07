import socket

host = "127.0.0.1"
port = 4444
sent = False

try:
    sock = socket.socket()
    sock.connect((host, port))

except socket.error:
    print("[*] An error occurred")
    exit(-1)

while(True):
    try:
        msg = input("[*] Enter your message: ")
        if(msg != ""):
            sock.send(str.encode(msg))
        
        rmsg = str(sock.recv(256).decode())
        if(rmsg != ""):
            print("[*] Received message: " + rmsg)

    except:
        print()
        print(f"[*] Exception raised, exiting...")
        sock.close()
        exit(0)