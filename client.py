import socket

def test_client():
    HOST, PORT = "localhost", 9999
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        print("Connecting to server...")
        sock.connect((HOST, PORT))
        print("Connected to server.")
       
        message = input("Enter a command followed by a message: ")
        
        # send user's input to the server
        sock.sendall(message.encode("utf-8"))
        
        # receive the response from the server
        received = sock.recv(1024).decode("utf-8")
        print(f"Received from server: {received}")

if __name__ == "__main__":
    while 1:
        test_client()