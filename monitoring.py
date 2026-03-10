import subprocess
import shutil
from config import servers, disk_threshold, log_file

def check_servers():
    print("\n--- Server Status ---")

    for server in servers:
        result = subprocess.run(
            ["ping", "-c", "1", server],
            stdout=subprocess.DEVNULL
        )

        if result.returncode == 0:
            print(f"[OK] {server} is reachable")
        else:
            print(f"[ALERT] {server} is DOWN")


def check_disk():
    print("\n--- Disk Usage ---")

    total, used, free = shutil.disk_usage("/")
    percent = (used / total) * 100

    print(f"Disk usage: {percent:.2f}%")

    if percent > disk_threshold:
        print("[WARNING] Disk usage above threshold")


def analyze_logs():
    print("\n--- Log Analysis ---")

    error_count = 0

    with open(log_file, "r") as file:
        for line in file:
            if "ERROR" in line:
                print("[ERROR]", line.strip())
                error_count += 1

    print(f"Total errors detected: {error_count}")


def main():
    print("Mini DevOps Monitoring System")
    print("=============================")

    check_servers()
    check_disk()
    analyze_logs()


if __name__ == "__main__":
    main()
