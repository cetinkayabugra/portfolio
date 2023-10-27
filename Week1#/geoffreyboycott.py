#!/usr/bin/python3

if __name__ == '__main__':
    pass


matches = 609
batted = 1014
not_out = 162
runs = 48426


completed_innings = batted - not_out
batting_average = runs / completed_innings


print(f"Geoffrey Boycott's batting average is: {batting_average}")
