# Remote Shell

A Python-based remote shell that uses **socket**, **subprocess**, and **platform** libraries to establish a connection between a client and server, allowing the server to send commands to the client to execute.

## Features

- Establishes a connection between a client and server using **sockets**.
- Server sends commands to be executed on the client machine.
- Executes commands on the client using **subprocess** and returns the output.
- Works cross-platform (supports Windows, Linux, and macOS).

## Technologies

- Python 3.x
- Socket (for client-server communication)
- Subprocess (for executing commands on the client)
- Platform (to check the client's OS)

## Setup and Usage

### Server Side

1. Make sure you have Python 3.x installed on your system.
2. Run the server script to listen for incoming connections:

```bash
python server.py
```
### Client Side
1. On the client machine, make sure Python 3.x is installed.
2. Run the client script to connect to the server:
```
python client.py
```
3. Once the client is connected, the server can send commands to be executed on the client machine.

Note: Ensure that both the server and client machines are on the same network or the server is accessible by the client.
