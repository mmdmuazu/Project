from collections import defaultdict

# Dictionary to count failed login attempts
user_attempts = defaultdict(int)

# Open the log file
with open("/var/log/auth.log", "r") as file:
    for line in file:
        if "password check failed for user" in line:
            # Extract the username from the line
            start = line.find("(") + 1
            end = line.find(")")
            username = line[start:end]
            user_attempts[username] += 1

# Show users with 3 or more failed attempts
for user, count in user_attempts.items():
    if count >= 3:
        print(f"[!] ALERT: User '{user}' had {count} failed login attempts.")
