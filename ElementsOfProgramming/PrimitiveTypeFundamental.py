#Write a program to count the number of bits that are set to 1 in a positive integer.
#Start with least-significant bit.
#Shows shiftign and masking

#common bitwise operators are: & , |, ^, ~, <<, >> (Noted: Python does not have concept of unsigned shift)
def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

print(count_bits(5))