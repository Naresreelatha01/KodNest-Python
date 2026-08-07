name = input()
course = input()
score = int(input())

# Create the tuple
student_record = (name, course, score)

# Unpack the tuple
unpacked_name, unpacked_course, unpacked_score = student_record

# Display the unpacked values
print(f"Name: {unpacked_name}")
print(f"Course: {unpacked_course}")
print(f"Score: {unpacked_score}")