stocks = {}
stocks["info"] = [600, 630, 620]
stocks["ril"] = [1430, 1490, 1567]
stocks["mtl"] = [234, 180, 160]

while True:
    ip = input("print, add (submit any other to exit): ")
    if ip == "print":
        for i, j in stocks.items():
            print(i, "==>", j, "==>", "avg: ", round(sum(j)/len(j),2))
    elif ip == "add":
        ip = input("Enter Stock name: ")
        if ip in stocks:
            stocks[ip].append(int(input("Enter price: ")))
        else:
            stocks[ip] = [int(input("Enter Price: "))]
    else:
        break