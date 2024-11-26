import socket

hostname = input ('Enter a domain name: ')
ip_add = socket.gethostbyname(hostname)

print(f'Domain Name: {hostname}')
print(f'IP Address: {ip_address}')
