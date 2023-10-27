#!/usr/bin/env python3

if __name__ == '__main__':
    pass

sweets = int(input("Counted sweets: "))
pupils = int(input("Attended pupils: "))

div_sweets = sweets // pupils
left_sweets = sweets % pupils

print("Each pupil will receive", div_sweets, "sweets.")
print("There will be", left_sweets, "sweets left over.")