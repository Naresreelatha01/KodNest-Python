# Read how many numbers will be entered
number_count = int(input())

# Initialize the counters and total
positive_count = 0
negative_count = 0
zero_count = 0
total = 0

# Read and analyze each number
for i in range(number_count):
    num = int(input())
    total += num
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

# Display the final analysis
print(f"Positive Count: {positive_count}")
print(f"Negative Count: {negative_count}")
print(f"Zero Count: {zero_count}")
print(f"Total: {total}")