import socket
import time
import threading
# they are open or closed. It uses the socket library to attempt connections
# to each port in the specified range and reports the status of each port.
# get target
target = input("Enter IP address or hostnameto scan: ")
start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))

# start timer
start_time = time.time()
# This code snippet scans a list of ports on a given IP address or hostname and checks if

#scan ports
for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # timeout after 1 second
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open on {target}.")
    else:
        print(f"Port {port} is closed on {target}.")
    sock.close()
start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))
# It uses the socket library to attempt connections to each port in the
# specified range and reports the status of each port.
ports = [22, 80, 443]
for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1) # timeout after 1 second
    result = sock.connect_ex(("208.80.152.201", port))
    if result == 0:
        print(f"Port {port} is open on {target}.")
    else:
        print(f"Port {port} is closed on {target}.")
    sock.close()
for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # timeout after 1 second
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open on {target}.")
    else:
        print(f"Port {port} is closed on {target}.")
    sock.close()
    target = input("Enter an IP address or hostname to scan: ").strip()

if not target:
    print("No IP or hostname entered. Exiting...")
    exit()
    
    def scan_port(target, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN ✅")
            sock.close()
        except Exception as e:
            pass  # Optional: print or log the error if you want
    
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        thread.start()


# This code snippet scans a list of ports on a given IP address or hostname and checks if