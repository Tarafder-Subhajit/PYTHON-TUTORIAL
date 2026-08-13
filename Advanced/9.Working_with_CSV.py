# CSV = Comma Separated Values

# Read
import csv

with open("servers.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# Skip the Header Row

with open("servers.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print(row)

# Access specific column

with open("servers.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print("Server:", row[0])
        print("IP:", row[1])

# Using DictReader (Recommended)

with open("servers.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["Server"], row["IP"])

# Write Data to a CSV

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Server", "Status"])

    writer.writerow(["web01", "Running"])
    writer.writerow(["web02", "Stopped"])

# Append new rows in output.csv

with open("output.csv", "a", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["db01", "Running"])