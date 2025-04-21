import socket

def dns_query(domain):
    # Create and send DNS query to Google's DNS server
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(3)  # Prevent hanging if no response
    
    # Build minimal DNS query
    query = b'\xAA\xAA\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00'  # Header
    for part in domain.split('.'):
        query += bytes([len(part)]) + part.encode()
    query += b'\x00\x00\x01\x00\x01'  # End of name, type A, class IN
    
    # Send query and get response
    sock.sendto(query, ('8.8.8.8', 53))
    try:
        response, _ = sock.recvfrom(512)
        # Extract IP from end of response (last 4 bytes for A record)
        ip = '.'.join(map(str, response[-4:]))
        return ip
    except:
        return "Query failed"
    finally:
        sock.close()

if __name__ == '__main__':
    domain = input('Enter domain: ')
    print('IP address:', dns_query(domain))
