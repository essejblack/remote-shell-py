import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)

print("Server is waiting for a client to connect...")
connection, addr = server.accept()
print(f"Client connected from {addr}")

try:
    while True:
        command = input("Enter command to execute on client ('exit' to quit): ")
        connection.sendall(command.encode())

        if command.lower() == 'exit':
            break

        response = connection.recv(16384)
        print("Client response:")
        print(response.decode(errors='ignore'))

except Exception as e:
    print(f"Error: {e}")

finally:
    connection.close()
    server.close()
    print("Server closed.")
