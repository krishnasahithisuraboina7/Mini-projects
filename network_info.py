import socket

# Get hostname and IP
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("Hostname:", hostname)
print("IP Address:", ip_address)

# Port scanning
target = "127.0.0.1"
print("\nScanning ports on", target)

for port in range(1, 100):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    s.close()