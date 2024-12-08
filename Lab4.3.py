# Generate 2 lists (course code and course name). create a new list with both course code and name like
# ["CS1001:Python",...]

course_codes = list(str(input("Enter the Course Codes: ")).split())

course_names = list(str(input("Enter the corresponding Course Names: ")).split())

course_details = [f"{code}:{name}" for code, name in zip(course_codes, course_names)]

print(course_details)
