import socket
import threading

# Get user input for target and port range
target = input("Enter an IP address or hostname to scan: ").strip()

if not target:
    print("No IP or hostname entered. Exiting...")
    exit()

start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))

# Function to scan a single port
def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        sock.close()
    except Exception as e:
        pass  # Optional: print or log the error if you want

# Scan specific ports
ports = [22, 80, 443]
for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # timeout after 1 second
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open on {target}.")
    else:
        print(f"Port {port} is closed on {target}.")
    sock.close()

# Scan port range
for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # timeout after 1 second
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open on {target}.")
    else:
        print(f"Port {port} is closed on {target}.")
    sock.close()

# Threaded scanning (optional)
for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(target, port))
    thread.start()

