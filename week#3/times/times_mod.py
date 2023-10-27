#!/usr/bin/env python3

if __name__ == '__main__':
    pass

num2 = int(input("Enter the number for the times table (0 to 12): "))
if 0 <= num2 <= 12:
    

    for num in range(13):
        result = num * num2
        print(f"{num} x {num2} = {result}")
