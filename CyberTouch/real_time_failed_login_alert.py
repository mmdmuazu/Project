import subprocess
from collections import defaultdict
import time

user_attempts = defaultdict(int)

# Use tail -F to watch the log file in real-time
process = subprocess.Popen(
    ['tail', '-F', '/var/log/auth.log'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

print("🔍 Watching /var/log/auth.log for failed login attempts...")

try:
    for line in process.stdout:
        decoded_line = line.decode('utf-8')
        if "password check failed for user" in decoded_line:
            start = decoded_line.find("(") + 1
            end = decoded_line.find(")")
            user = decoded_line[start:end]
            user_attempts[user] += 1

            if user_attempts[user] == 3:
                print(f"\n🚨 ALERT: User '{user}' failed login 3 times!\n")
except KeyboardInterrupt:
    print("🛑 Stopped monitoring.")
