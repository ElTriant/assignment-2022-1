import sys
import math
import hashlib

if len(sys.argv) != 2:
    print("Program argument incorrect.")
    exit()

exampleFile = sys.argv[1]

given_file = open(exampleFile, 'r')

a = True
s = 0
U = bytearray()
L = bytearray()
numbers = []

lines = given_file.readlines()

for line in lines:
    numbers.append(line)
    #check if list is sorted
    line = int(line)
    if line < s:
        a = False
    s = line

given_file.close()

if a == False:
    print("List in not sorted.")
    exit()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

#print(numbers)

#find the number l
n = len(numbers)
m = max(numbers)
lbn = math.floor(math.log2(m/n))

print("l ", lbn)

byte_array = bytearray(numbers)

def create_L(barray):
    for i in barray:
        barray[i] = barray[i] << 8 - lbn
