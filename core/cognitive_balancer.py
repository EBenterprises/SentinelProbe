import psutil
import socket

def get_node_score():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    return (cpu * 0.7) + (mem * 0.3)

def broadcast_health():
    score = get_node_score()
    # Broadcast score to cluster via UDP multicast
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    sock.sendto(str(score).encode(), ("224.1.1.1", 5005))

if __name__ == "__main__":
    broadcast_health()
