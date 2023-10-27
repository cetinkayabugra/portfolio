#!/usr/bin/env python3

if __name__ == '__main__':
    pass

num_students = int(input("How many students? "))
group_size = int(input("Required group size? "))


num_groups = num_students // group_size
num_left_over = num_students % group_size


print("There will be", num_groups, "groups with", num_left_over, "students left over.")