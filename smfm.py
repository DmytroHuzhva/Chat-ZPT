import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip2 = s.getsockname()[0]
s.close()


def print(ip2):
    pass


print(ip2)

