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

#find the number l
n = len(numbers)
m = max(numbers)
lbn = math.floor(math.log2(m/n))

print("l ", lbn)

size_U = math.ceil((n * (9 - lbn))/8)
U = bytearray(size_U)
size_L = math.ceil((n*lbn)/8)
L = bytearray(size_L)
digit_U = 7
digit_L = 7
row_U = 0
row_L = 0
num_left = 0
num_right = 0
prev_num = 0
new_num = 0

for i in range(0, n):

    temp = numbers[i]

    #creating table L
    mask = int(math.pow(2, lbn) - 1)
    num_right = temp & mask

    for y in range(lbn, 0, -1):
        temp_2 = int(math.pow(2, y - 1)) & num_right
        if temp_2 > 1:
            temp_2 = 1
        temp_3 = temp_2 * int(math.pow(2, digit_L))
        L[row_L] = (L[row_L] + temp_3) % 256
        digit_L -= 1
        if digit_L == -1:
            digit_L = 7
            row_L += 1

    #creating table U
    num_left = int(temp / int(math.pow(2, lbn)))
    new_num = int(num_left - prev_num)
    prev_num = num_left

    for y in range(0, new_num):
        digit_U -= 1
        if digit_U == -1:
            row_U += 1
            digit_U = 7

    temp_2 = int(math.pow(2, digit_U))
    digit_U -= 1
    if digit_U == -1:
        row_U += 1
        digit_U = 7
    U[row_U] = (U[row_U] | temp_2) % 256

#print table L
print('L')
for i in range(0, size_L):
    temp = L[i]
    str = ''
    for y in range(8, 0, -1):
        mask = int(math.pow(2, y - 1))
        temp_2 = temp & mask
        if temp_2 == 0:
            str = str + '0'
        else:
             str = str + '1'
    print(str)

#print table U
print('U')

for i in range(0, row_U + 1):
    temp = U[i]
    str = ''
    for y in range(0, 8):
        mask = int(math.pow(2, 7 - y))
        temp_2 = temp & mask
        if temp_2 == 0:
            str = str + '0'
        else:
             str = str + '1'
    print(str)

# Create SHA-256 digest of L and U
h = hashlib.sha256()
h.update(L)
h.update(U)
digest = h.hexdigest()
print(digest)
