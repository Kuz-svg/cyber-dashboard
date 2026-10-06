import socket

print("==============================\n       CYBER DASHBOARD\n==============================")

domain = input("Enter target: ")

ip = socket.gethostbyname(domain)

print("Target:", domain)
print("Resolved IP:", ip)