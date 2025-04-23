import socket

def scan_ports(target, ports):
    print(f"\nScanning target: {target}")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is open.")
            sock.close()
        except Exception as e:
            print(f"[-] Error scanning port {port}: {e}")

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    port_range = input("Enter ports to scan (e.g., 20-80): ")

    start_port, end_port = map(int, port_range.split("-"))
    ports_to_scan = range(start_port, end_port + 1)

    scan_ports(target_ip, ports_to_scan)
