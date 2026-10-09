import socket

print("==============================\n       CYBER DASHBOARD\n==============================")

domain = input("Enter target: ")

try:
    result = socket.gethostbyname_ex(domain)
    ips = result[2]
    print("Resolved IP:")
    for ip in ips:
        print(ip)
    print(f"Total IPv4 addresses: {len(ips)}")

except socket.gaierror:
    print("Could not resolve domain")
    