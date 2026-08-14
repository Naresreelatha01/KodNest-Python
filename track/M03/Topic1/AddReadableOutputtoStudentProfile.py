class StudentProfile:
    def __init__(
        self,
        student_id,
        name,
        course,
        experience,
        skills
    ):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience
        self.skills = skills

    def __str__(self):
        # Format the skills list as a comma-separated string
        skills_str = ", ".join(self.skills)
        
        # Return the multi-line profile string
        return (
            f"STUDENT PROFILE\n"
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Course: {self.course}\n"
            f"Experience in Years: {self.experience}\n"
            f"Skills: {skills_str}"
        )

# Read inputs
student_id = int(input())
name = input().strip()
course = input().strip()
experience = int(input())
skills = input().split()

# Create one StudentProfile object
student = StudentProfile(student_id, name, course, experience, skills)

# Display the object using print(student)
print(student)