#############
# CONSTANTS
#############

FILENAME = "records.txt"

#############
# GLOBAL VARS
#############

file = None
record = []

#############
# MAIN
#############

ID = input()
file = open(FILENAME, "r")

for line in file:
  record = line.split(",")
  if record[0] == ID:
    print(record[1])
    break

file.close()
