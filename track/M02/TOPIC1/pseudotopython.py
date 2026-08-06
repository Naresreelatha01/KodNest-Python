# Read the limit
lim = int(input())

# Initialize the loop variable and total
num = 1
tot = 0

# Examine every number from 1 to limit
while num <= lim:
    if num % 2 == 0:
        tot += num
    num += 1

# Display the result
print("Even Sum:", tot)