# Define the binary number as a string
binary_number_1 = '11111111'
binary_number_2 = '10001001'

# Convert the binary string to an integer
number_1 = int(binary_number_1, 2)
number_2 = int(binary_number_2, 2)

# 1
# Perform a left shift by 1 bit
result = number_1 << 1

# Convert the result back to a binary string, removing the '0b' prefix
result_binary = bin(result)[2:]

print("Result 1", result_binary)

# 2
result = number_2 >> 1
result_binary = bin(result)[2:]
print("Result 2", result_binary)

# 3
print("Result 3", bin(number_1 * number_2)[2:])

# 4
print("Result 4", bin(number_1 | number_2)[2:])

# 5
print("Result 5", bin(number_1 + number_2)[2:])

# 6
print("Result 6", bin(number_1 & number_2)[2:])

# 7
# bin to hex
print("Result 7", hex(int(bin(number_1 & number_2)[2:], 2))) #89
