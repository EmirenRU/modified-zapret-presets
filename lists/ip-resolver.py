import subprocess
import platform
import re

def ping_ip(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '4', ip]

    try:
        output = subprocess.check_output(command, universal_newlines=True)
        print(output)
        avg_time = re.search(r'Average = (\d+)ms', output) if platform.system().lower() == 'windows' else re.search(
            r'avg = (\d+\.\d+)', output)
        if avg_time:
            return float(avg_time.group(1))
    except subprocess.CalledProcessError:
        return float('inf')
    return float('inf')

def find_best_ip(ips):
    best_ip = None
    best_time = float('inf')

    for ip in ips:
        print(f"Pinging {ip}...")
        ping_time = ping_ip(ip)
        print(f"Response time for {ip}: {ping_time} ms")

        if ping_time < best_time:
            best_time = ping_time
            best_ip = ip

    return best_ip, best_time

if __name__ == "__main__":
    ip_addresses = [
    "208.89.73.17",
    "208.89.73.19",
    "208.89.73.21",
    "208.89.73.23",
    "208.89.73.25",
    "208.89.73.27",
    "208.89.73.29",
    "208.89.73.31",
    "23.210.73.5",
    "23.210.73.6",
    "208.89.73.31",
    "208.89.73.27",
    "208.89.73.23",
    "208.89.73.25",
    "208.89.73.21",
    "208.89.73.19",
    "208.89.73.17",
    "208.89.73.29",
    "151.101.42.172",
    "199.232.210.172",
    "199.232.214.172",
    "23.44.229.228",
    "23.44.229.226",
    "23.44.229.202",
    "23.44.229.208",
    "23.44.229.203",
    "23.44.229.206",
    "199.232.66.172",
    "92.223.118.251",
    "151.101.126.172",
    "151.101.62.172",
    "93.123.17.252",
    "2.17.112.225",
    "2.17.112.205",
    "185.160.60.100",
    "208.89.74.17",
    "208.89.74.19",
    "208.89.74.27",
    "208.89.74.23",
    "208.89.74.21",
    "208.89.74.29",
    "208.89.74.31",
    "8.243.208.233",
    "8.243.208.235",
    "92.223.98.98",
    "109.61.38.38",
    "199.232.210.172",
    "199.232.214.172",
    "93.123.11.59",
    "151.101.30.172",
    "109.61.38.38",
    "92.223.63.254",
    "43.152.143.98",
    "43.174.32.224",
    "43.174.32.117",
    "43.174.32.211",
    "43.174.32.88",
    "43.174.32.194",
    "43.152.143.190",
    "43.174.32.150",
    "43.152.143.189",
    "43.174.53.240",
    "43.174.51.113",
    "43.174.32.212",
    "43.174.32.193",
    "43.174.51.112",
    "91.80.49.86",
    "91.81.129.182",
    "91.81.130.134",
    "91.80.49.20",
    "91.81.129.181",
    "92.223.116.252",
    "213.202.3.240",
    "199.232.26.172",
    "92.223.95.95"
    ]

    best_ip, best_time = find_best_ip(ip_addresses)
    print(f"\nBest IP: {best_ip} with a ping time of {best_time} ms")
