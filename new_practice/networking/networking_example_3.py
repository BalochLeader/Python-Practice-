# Networking Example 3
# This program demonstrates a simple client-side socket connection.
# Note: This requires a server to connect to. For demonstration, it will try to connect to a non-existent server.

import socket

host = 'localhost'
port = 12345

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to {host}:{port}")
    client_socket.sendall(b"Hello, server!")
    data = client_socket.recv(1024)
    print(f"Received from server: {data.decode()}")
    client_socket.close()
except ConnectionRefusedError:
    print(f"Connection refused. Make sure a server is running on {host}:{port}")
except Exception as e:
    print(f"An error occurred: {e}")
