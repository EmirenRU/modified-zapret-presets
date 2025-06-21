def scan(keyword):
    res = set()
    with open("list-general-big.txt", 'r') as file:
        for line in file:
            if keyword in line:
                res.add(line)

    for line in res:
        print(line)

if __name__ == "__main__":
    scan(input("Enter keywords: "))