import socket

def http_header_viewer(host):
    try:
        # Create socket and connect
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((host, 80))
        
        # Send HTTP HEAD request
        s.sendall(f"HEAD / HTTP/1.1\r\nHost: {host}\r\n\r\n".encode())
        
        # Get and display response
        response = s.recv(4096).decode()
        print(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        s.close()

if __name__ == '__main__':
    host = input("Enter host (e.g., example.com): ")
    http_header_viewer(host)
