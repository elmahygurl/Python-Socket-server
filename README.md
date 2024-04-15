# SocketServer Word and Character Counter

## Description
This project implements a server using Python's `socketserver` module to count the number of words and characters in a string sent by a client. Additionally, the server performs specific operations based on the first character of the string received from the client.

## Features
- Accepts client connections and receives strings
- Counts the number of words and characters in the string
- Performs operations based on the first character of the string:
  - 'W': Returns the number of words
  - 'L': Returns the number of lowercase letters
  - 'U': Returns the number of uppercase letters
  - 'R': Returns the number of numeric characters
  - 'T': Returns the total number of characters
- Handles exceptions and special cases

## How to Use
1. **Server Creation**: Run the Python script containing the server implementation.
2. **Client Interaction**: Connect to the server using a client script or tool such as telnet.
3. **Sending Requests**: Send strings containing one of the specified operations ('W', 'L', 'U', 'R', 'T') followed by a space and the string to be analyzed.
4. **Receiving Responses**: Receive responses containing the requested count or the original message if the operation is invalid.

## Running the Client
To run the client script, execute the following command in your terminal or command prompt:

```bash
py client.py
```

## Implementation Steps
1. **Import the SocketServer Module**: `import socketserver`
2. **Create a Server Class**: Create a server class inheriting from `socketserver.TCPServer`.
3. **Create a Request Handler Class**: Subclass `socketserver.BaseRequestHandler` and override the `handle()` method to process incoming requests.
4. **Instantiate the Server Class**: Instantiate the server class, providing the server's address and the request handler class.
5. **Start the Server**: Call `serve_forever()` method of the server object to process requests.
6. **Stop the Server**: Call `shutdown()` method to stop the server.

## Testing
- **Test 1**: Input: "Wpython Socket Server". Expected Output: "The number of words is 3"
- **Test 2**: Input: "LpythonSocketServer". Expected Output: "The number of lowercase letters is 16"
- **Test 3**: Input: "UPYTHONSOCKETSERVER". Expected Output: "The number of uppercase letters is 18"
- **Test 4**: Input: "R1234567890". Expected Output: "The number of numeric characters is 10"
- **Test 5**: Input: "TpythonSocketServer123". Expected Output: "The total number of characters is 22"
- **Test 6**: Input: "pythonSocketServer123". Expected Output: "pythonSocketServer123"

## Sample Run
![image](https://github.com/elmahygurl/Python-Socket-server/assets/97133077/264ea4ea-ed68-49ed-800a-25128731a730)

![image](https://github.com/elmahygurl/Python-Socket-server/assets/97133077/3015da3d-ca9f-4337-b566-7bb1a2fb6213)


## Network Traffic Analysis
A screenshot of Wireshark showing the traffic between the server and client will be provided as part of the project documentation.
![Capture1](https://github.com/elmahygurl/Python-Socket-server/assets/97133077/9911f48e-ca6f-45f0-80df-f45ad780aa9c)

