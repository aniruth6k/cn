import socket

def daytime_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('time.nist.gov', 13)  # NIST daytime server
    try:
        client_socket.connect(server_address)
        time_data = client_socket.recv(1024).decode()
        print("Current time from server:", time_data.strip())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == '__main__':
    daytime_client()
