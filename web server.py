import socket

def simple_web_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 8080))
    server_socket.listen(1)
    print("Web Server is running on http://127.0.0.1:8080")
    
    try:
        while True:
            client_connection, client_address = server_socket.accept()
            request = client_connection.recv(1024).decode()
            
            # Fixed the HTML response string (it was broken across lines)
            response = "HTTP/1.1 200 OK\n\n<html><body><h1>Hello, World!</h1></body></html>"
            
            client_connection.sendall(response.encode())
            client_connection.close()
    except KeyboardInterrupt:
        print("\nShutting down the server...")
    finally:
        server_socket.close()

if __name__ == '__main__':
    simple_web_server()
