import socket
from crypto_mesh import decrypt_mesh

def listen_for_nodes():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 5003))
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Node detected at {addr}: {data.decode()}")

if __name__ == "__main__":
    listen_for_nodes()
