import socket
import argparse
import threading
from queue import Queue
import ipaddress
from tqdm import tqdm
from ping3 import ping

"""
Port Scanner Script
Usage: python script.py <ip> <ports>
Example: python script.py 127.0.0.1 80 443 8000:8100
"""

def test_tcp(ip, port):
    """
    Test if a TCP port is open by attempting to establish a connection.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        result = sock.connect_ex((ip, port))
        return result == 0
    except Exception:
        return False
    finally:
        sock.close()

def test(ip, port, services):
    """
    Test if a TCP port is open and print the result.
    """
    if not (0 <= port <= 65535):
        message = f"Invalid port number: {port}"
        tqdm.write(message)
        return

    result = test_tcp(ip, port)

    service_name = services.get((str(port), 'tcp'), 'Unknown service')

    if result:
        message = f"Port {port} (TCP) is open ({service_name})"
        tqdm.write(message)

def portscan(ip, ports, services):
    """
    Run a port scan on the given IP with a progress bar.
    """
    port_list = []

    for port in ports:
        if ':' in port:
            start, end = port.split(':')
            for p in range(int(start), int(end) + 1):
                port_list.append(int(p))
        else:
            port_list.append(int(port))

    progress_bar = tqdm(total=len(port_list), desc="Scanning Ports")

    port_queue = Queue()

    for port in port_list:
        port_queue.put(port)

    def worker():
        while True:
            try:
                port = port_queue.get_nowait()
            except Exception:
                break
            test(ip, port, services)
            port_queue.task_done()
            progress_bar.update(1)

    num_threads = 100 
    for _ in range(num_threads):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

    port_queue.join()
    progress_bar.close()

def load_services():
    """
    Load the services from the /etc/services file.
    """
    services_dict = {}
    try:
        with open('/etc/services') as f:
            for line in f:
                if line.startswith('#') or not line.strip():
                    continue
                parts = line.split()
                if len(parts) >= 2:
                    service_name = parts[0]
                    port_proto = parts[1]
                    if '/' in port_proto:
                        port, protocol = port_proto.split('/')
                        services_dict[(port, protocol)] = service_name
        return services_dict
    except IOError as e:
        print(f"Error reading /etc/services: {e}")
        return {}

def is_ip_connectable(ip):
    """
    Check if the IP address is connectable by sending an ICMP ping using ping3.
    """
    response_time = ping(ip, timeout=4)
    return response_time is not None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Port Scanner')
    parser.add_argument("ip", help="IP address to scan")
    parser.add_argument("ports", help="Ports to scan (e.g., 80 443 20:25)", nargs="+")
    args = parser.parse_args()

    try:
        ipaddress.ip_address(args.ip)
    except ValueError:
        print(f"Invalid IP address: {args.ip}")
        exit(1)

    if not is_ip_connectable(args.ip):
        print(f"The IP address {args.ip} is not reachable.")
        exit(1)

    services = load_services()

    portscan(args.ip, args.ports, services)
