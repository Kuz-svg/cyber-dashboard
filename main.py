import socket

print("==============================\n       CYBER DASHBOARD\n==============================")

domain = input("Enter target: ")

try:
    ip = socket.gethostbyname(domain)
    print("Target:", domain)
    print("Resolved IP:", ip)

except socket.gaierror:
    print("Could not resolve domain")

