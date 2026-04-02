a = 132
b = 45
n = 35  # Set a line width
fmt0 = '{:<10}'
fmt1 = '0b{:08b} 0x{:02x} {:3}'

print("bitwise AND:")
print(fmt0.format('a'), fmt1.format(a, a, a))
print(fmt0.format('b'), fmt1.format(b, b, b))
print('-' * n)
# The result of the AND operation
print(fmt0.format('a & b'), fmt1.format(a & b, a & b, a & b))

