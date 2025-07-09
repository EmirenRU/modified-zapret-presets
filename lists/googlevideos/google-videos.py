import socket
from multiprocessing import Pool

def resolve_ip(url):
    try:
        ip = socket.gethostbyname(url)
        return url, ip
    except socket.gaierror:
        return None

def check_ip(f):
    with open(f, 'r') as file:
        urls = [line.strip() for line in file]

    with Pool() as pool:
        results = pool.map(resolve_ip, urls)

    with open(f + '-clean.txt', 'w') as file:
        for result in results:
            if result:
                name, ip = result
                file.write(f'{ip} {name}\n')

if __name__ == "__main__":
    check_ip('googlevideos.txt')