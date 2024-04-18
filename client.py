import socket
import serial

def connect_to_serial_server(server_ip, server_port):
    try:
        # Create a socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the serial server
        client_socket.connect((server_ip, server_port))
        print("Connected to serial server")

        ser = serial.Serial('COM1', 115200, timeout=0.05)
        # ser.open()
        while True:
            request = ser.read(256)
            if len(request)>0:
                # Send request to the server
                print("Request data:", request)
                client_socket.send(request)
                # Receive data from the server
                response = client_socket.recv(1024)  # Receive up to 1024 bytes of data
                print("Received data:", response)
                ser.write(response)

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        # Close the socket
        client_socket.close()


def main():
    # Serial server configuration
    serial_server_ip = '0.0.0.0'   # rpi address
    serial_server_port = 12345

    # Connect to the serial server
    connect_to_serial_server(serial_server_ip, serial_server_port)

if __name__ == "__main__":
    main()
