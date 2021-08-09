import socket,rsa,json


# Class Client
class Client:
    def __init__(self):

        self.encoder = "utf-8"
        self.ip = "localhost"
        # self.port = 1234
        self.buffer = 4096


        # Create Socket
        try: 
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            print ("Socket successfully created")
        except socket.error as err: 
            print ("Socket creation failed with error %s" %(err))
    


    def send(self,server,msg):
        self.s.connect(server)

        self.s.send((msg).encode("utf-8"))

        data_from_server = self.s.recv(self.buffer)
        self.s.close()
        return data_from_server
        






# Main
c = Client()
server = ('localhost',1234)
data = c.send(server,"Hello server")
print(data)

# while 1:
#     try:
#         continue
#     except KeyboardInterrupt:
#         print("\nExiting ...\n")
#         break