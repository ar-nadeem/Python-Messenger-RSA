import socket,rsa,json

##################################### SERVER #######################################
class Server:
    def __init__(self):

        self.encoder = "utf-8"
        self.ip = "localhost"
        self.port = 1234
        self.buffer = 4096

        # Create Socket
        try: 
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

            self.s.bind((self.ip, self.port))

            print ("Socket successfully created")
        except socket.error as err: 
            print ("Socket creation failed with error %s" %(err))
    

    def listen(self,):
        # Set socket to listening mode
        self.s.listen(5)
        
        # Accept connection
        
        (conn,addr) = self.s.accept() # Accept connection
        data_from_client = conn.recv(self.buffer)
        return(data_from_client,conn,addr)


    def send_to_conn(self,conn,msg):
        conn.send((msg).encode(self.encoder))
    
    def close_conn(self,conn):
        conn.close()
        return True
        

# Main
server = Server()

data = "".encode(server.encoder)
while not data:
    data,conn,addr = server.listen()

server.send_to_conn(conn,"Hello Cleint")
server.close_conn(conn)

# while 1:
#     try:
#         continue
#     except KeyboardInterrupt:
#         print("\nExiting ...\n")
#         break