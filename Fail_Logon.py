# failed_login_check.py
import re
from collections import defaultdict

def parse_failed_logins(log_file_path):
    failed_logins = defaultdict(int)
    pattern = re.compile(r"LOGIN FAILED for user:\s*(\S+)")

    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                match = pattern.search(line)
                if match:
                    username = match.group(1)
                    failed_logins[username] += 1
    except FileNotFoundError:
        print(f"Error: Log file '{log_file_path}' not found.")
        return {}

    return failed_logins

def print_failed_logins_summary(failed_logins):
    print("\n--- Failed Login Attempts Summary ---")
    if not failed_logins:
        print("No failed login attempts found.")
        return
    for user, count in failed_logins.items():
        print(f"User: {user} - Failed Attempts: {count}")

if __name__ == "__main__":
    log_file = "auth.log"  # Change this to your log file path
    failed_logins = parse_failed_logins(log_file)
    print_failed_logins_summary(failed_logins)


