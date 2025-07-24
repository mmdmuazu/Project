from collections import defaultdict

ip_counts = defaultdict(int)

with open("auth.log","r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()
            ip = parts[-4]
            ip_counts[ip] += 1

for ip, count in ip_counts.items():
    if count >= 3:
        print(f"[!] Possible brute-force attack from {ip} ({count} attempts)")