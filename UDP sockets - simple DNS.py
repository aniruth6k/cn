import socket
import struct

# DNS server info (Google's public DNS)
DNS_SERVER_IP = '8.8.8.8'
DNS_SERVER_PORT = 53

def build_query(domain):
    # Transaction ID
    transaction_id = b'\xaa\xaa'
    
    # Flags: standard query
    flags = b'\x01\x00'
    
    # Questions: 1, other counts: 0
    counts = b'\x00\x01\x00\x00\x00\x00\x00\x00'
    
    # Encode domain parts
    query_parts = b''
    for part in domain.split('.'):
        query_parts += struct.pack('B', len(part)) + part.encode()
    
    # Terminating zero, type A (1), class IN (1)
    query_end = b'\x00\x00\x01\x00\x01'
    
    return transaction_id + flags + counts + query_parts + query_end

def parse_response(response):
    # Skip header (12 bytes) and question section to find answer
    i = 12
    while True:
        if i >= len(response) or response[i] == 0:
            break
        i += response[i] + 1
    
    # Skip null byte, qtype, and qclass (5 bytes)
    i += 5
    
    # If we have an answer section
    if i + 16 <= len(response):
        # Check if we have an A record (0x0001)
        if response[i+2:i+4] == b'\x00\x01':
            # IPv4 address is the last 4 bytes of standard A record
            ip_bytes = response[i+12:i+16]
            return socket.inet_ntoa(ip_bytes)
    
    return None

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(5)
    
    domain_name = input('Enter the domain name: ')
    
    try:
        # Send DNS query
        query = build_query(domain_name)
        client_socket.sendto(query, (DNS_SERVER_IP, DNS_SERVER_PORT))
        
        # Receive response
        response, _ = client_socket.recvfrom(1024)
        
        # Parse IP address
        ip_address = parse_response(response)
        if ip_address:
            print(f'{domain_name} resolves to {ip_address}')
        else:
            print(f'{domain_name} does not have an IP address')
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
