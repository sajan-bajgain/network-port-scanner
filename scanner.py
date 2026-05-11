import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # prevents hanging
        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
        else:
            print(f"[CLOSED] Port {port}")

        sock.close()

    except socket.error as e:
        print(f"Error scanning port {port}: {e}")


def scan_ports(ip, start_port, end_port):
    print(f"\nScanning {ip}...\n")

    for port in range(start_port, end_port + 1):
        scan_port(ip, port)


if __name__ == "__main__":
    target_ip = input("Enter target IP (e.g. 127.0.0.1): ")
    start = int(input("Start port: "))
    end = int(input("End port: "))

    scan_ports(target_ip, start, end)