open_file = open("Cupcakeinvoices.csv")

total = []

max_total = 0


for line in open_file:
    arr = line.split(",")
    print(arr[2])
    print (arr[4])
    print (arr[3])
    price = float(arr[4])
    quantity = float(arr[3])
    total = (price * quantity)
    print(total)
    max_total += total

print(max_total)

print(arr)


# for line in open_file:
#     totalSum = line.split(",")
#     print(totalSum[4])
