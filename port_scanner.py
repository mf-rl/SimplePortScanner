import socket
import sys
from datetime import datetime
import argparse

def scan_port(host, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            return sock.connect_ex((host, port)) == 0
    except (socket.gaierror, socket.error):
        return False

def scan_ports(host, start_port, end_port, timeout=1, verbose=False):
    try:
        target_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print(f"Error: Cannot resolve hostname '{host}'")
        sys.exit(1)
    
    print("-" * 60)
    print(f"Scanning: {host} ({target_ip}) | Ports: {start_port}-{end_port}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)
    
    open_ports = []
    
    try:
        for port in range(start_port, end_port + 1):
            if scan_port(target_ip, port, timeout):
                try:
                    service = f" ({socket.getservbyport(port)})"
                except OSError:
                    service = ""
                print(f"Port {port}: OPEN{service}")
                open_ports.append(port)
            elif verbose:
                print(f"Port {port}: CLOSED")
                
    except KeyboardInterrupt:
        print("\n\nScan interrupted by user.")
        sys.exit(0)
    
    print("-" * 60)
    print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Open ports: {len(open_ports)}" + (f" - {', '.join(map(str, open_ports))}" if open_ports else ""))
    print("-" * 60)

def main():
    parser = argparse.ArgumentParser(description='Simple Port Scanner')
    parser.add_argument('host', help='Target hostname or IP')
    parser.add_argument('-s', '--start', type=int, default=1, help='Start port (default: 1)')
    parser.add_argument('-e', '--end', type=int, default=1024, help='End port (default: 1024)')
    parser.add_argument('-t', '--timeout', type=float, default=1.0, help='Timeout in seconds (default: 1.0)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Show closed ports')
    args = parser.parse_args()
    
    if not (1 <= args.start <= args.end <= 65535):
        print("Error: Ports must be 1-65535 and start <= end")
        sys.exit(1)
    
    scan_ports(args.host, args.start, args.end, args.timeout, args.verbose)

if __name__ == "__main__":
    main()
