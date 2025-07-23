import socket
import threading

def is_valid_port(port):
    """Check if port is an integer and in valid range."""
    return isinstance(port, int) and 0 <= port <= 65535

def scan_port(target, port, show_closed=True):
    """Scan a single port and print result."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN on {target}")
            elif show_closed:
                print(f"Port {port} is CLOSED on {target}")
    except Exception as e:
        print(f"Error scanning port {port} on {target}: {e}")

def get_port_input(prompt):
    """Safely get a port number from user."""
    while True:
        try:
            value = int(input(prompt).strip())
            if is_valid_port(value):
                return value
            else:
                print("Port number must be between 0 and 65535.")
        except ValueError:
            print("Please enter a valid integer.")

def main():
    target = input("Enter an IP address or hostname to scan: ").strip()
    if not target:
        print("No IP or hostname entered. Exiting...")
        return

    # Resolve hostname to IP
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Could not resolve host: {target}")
        return

    start_port = get_port_input("Enter the starting port number: ")
    end_port = get_port_input("Enter the ending port number: ")
    if start_port > end_port:
        print("Start port must be less than or equal to end port. Exiting...")
        return

    print("\nScanning common ports (22, 80, 443):")
    common_ports = [22, 80, 443]
    for port in common_ports:
        scan_port(target_ip, port)

    method = input("\nScan ports using (s)equential or (t)hreaded? [s/t]: ").strip().lower()
    print(f"\nScanning ports {start_port} to {end_port} on {target_ip}:")
    if method == "t":
        threads = []
        for port in range(start_port, end_port + 1):
            t = threading.Thread(target=scan_port, args=(target_ip, port, False))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        print("Threaded scan complete.")
    else:
        for port in range(start_port, end_port + 1):
            scan_port(target_ip, port, False)
        print("Sequential scan complete.")

if __name__ == "__main__":
    main()