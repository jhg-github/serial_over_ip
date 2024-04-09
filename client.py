import socket

def connect_to_serial_server(server_ip, server_port):
    try:
        # Create a socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the serial server
        client_socket.connect((server_ip, server_port))
        
        print("Connected to serial server")

        # Now you can send and receive data over the network connection
        # For example, you can send data to the serial port using client_socket.send() 
        # and receive data using client_socket.recv()

        for _ in range(10):
            # Send data to the server
            data = "Hello, server! This is a message from the client."
            client_socket.send(data.encode('utf-8'))  # Encode and send the data
            # Receive data from the server
            data = client_socket.recv(1024)  # Receive up to 1024 bytes of data
            print("Received data:", data.decode('utf-8'))

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        # Close the socket
        client_socket.close()

def main():
    # Serial server configuration
    serial_server_ip = '192.168.1.175'  # rpi address
    serial_server_port = 12345
    
    # Connect to the serial server
    connect_to_serial_server(serial_server_ip, serial_server_port)

if __name__ == "__main__":
    main()
