import socketserver 

class MyTCPServer(socketserver.TCPServer):
    pass

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self): #overridden function
        # self.request is the TCP socket connected to the client

        self.data = self.request.recv(1024).strip().decode("utf-8")
        print(f"Received from {self.client_address[0]}: {self.data}")
        responsee = self.process_request(self.data) #calling the function to process the incoming request

        self.request.sendall(str(responsee).encode('utf-8')) #send response back to user

    def process_request(self, data): #function for conditions of commands
        code, text = data[0], data[1:] #seperate first character and rest of string

        if code == 'W':
            return f"The number of words is {len(text.split())}"
        elif code == 'L':
            return f"The number of lowercase letters is {sum(1 for char in text if char.islower())}"
        elif code == 'U':
            return f"The number of uppercase letters is {sum(1 for char in text if char.isupper())}"
        elif code == 'R':
            return f"The number of numeric characters is {sum(1 for char in text if char.isdigit())}"
        elif code == 'T':
            return f"The total number of characters is {len(text)+1}"  #include code charachter
        else:  #if code not recognised
            return data  






#set up server
HOST, PORT = "localhost", 9999
server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

#start server and keep it running till keyboard interrupt occurs
try:
    print(f"Server listening on {HOST}:{PORT}")
    server.serve_forever()
except KeyboardInterrupt:
    print("Server is shutting down.")
    server.shutdown()