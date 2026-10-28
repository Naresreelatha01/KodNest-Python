students = [
    ["Alice", 85, 90, 78],
    ["Bob", 70, 88, 92],
    ["Charlie", 95, 80, 89],
    ["David", 60, 75, 68],
    ["Eva", 88, 92, 95],
    ["Frank", 72, 65, 80],
    ["Grace", 90, 85, 91]
]
print("=== STUDENT REPORT ====")
for s in students:
  avg = sum(s[1:]) / len(s[1:])
  print(f"{s[0]} -- Average:{avg:.2f}")
  
top_students = [
    s[0] for s in students if s[1] >= 80 and s[2] >= 80 and s[3] >= 80
]

print(f"Top Students: {top_students}")

weak_students = [s[0] for s in students if s[1] < 70 or s[2] < 70 or s[3] < 70]
print(f"Students needing Improvement:{weak_students}")
