import socket
import serial


def start_serial_server(host, port):
    try:
        # Create a socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to the address and port
        server_socket.bind((host, port))
        # Start listening for incoming connections
        server_socket.listen(1)

        print(f"Serial server listening on {host}:{port}")
        ser = serial.Serial('/dev/usb_magna_geni', 115200, timeout=0.05)

        # Accept incoming connections
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection established with {client_address}")

            # Wait to receive data from the client
            while True:
                try:
                    request = client_socket.recv(1024)  # Receive up to 1024 bytes of data
                    if not request:
                        print(f"Client {client_address} closed the connection")
                        break  # No more data to receive, exit the loop
                    print("Request data:", request)
                    # Send request to serial port
                    ser.write(request)
                    while True:
                        response = ser.read(256)
                        if len(response) > 0:
                            print("Response data:", response)
                            break
                    # Send response to the client
                    client_socket.send(response)
                except ConnectionResetError:
                    print(f"Client {client_address} forcibly closed the connection")
                    break

            client_socket.close()

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        # Close the socket
        server_socket.close()

def main():
    # Server configuration
    server_host = '0.0.0.0'   # rpi address
    server_port = 12345  # Example port number

    # Start the serial server
    start_serial_server(server_host, server_port)

if __name__ == "__main__":
    main()
