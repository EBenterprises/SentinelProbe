import socket

def announce_presence():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    while True:
        sock.sendto(b"DISCOVERY_BEACON", ('<broadcast>', 5003))
        import time
        time.sleep(60)
