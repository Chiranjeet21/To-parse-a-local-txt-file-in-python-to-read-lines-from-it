# To parse a local txt file in python to read lines from it
# Step 1 Read file
sequence = open('Data.txt', 'r')
read = sequence.readlines()

NewList = []
for line in read:
    NewList.append(line.strip())

    print(NewList)
