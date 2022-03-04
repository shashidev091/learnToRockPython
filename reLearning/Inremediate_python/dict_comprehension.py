import random
# new_dict = { new_key:new_value for (key, value) item in dict.items() }

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# student_score = {name: random.randint(50, 99) for name in names}
student_score = {'Alex': 88, 'Beth': 83, 'Caroline': 71, 'Dave': 50, 'Eleanor': 86, 'Freddie': 61}

print(student_score)

passed_students = {name: marks for (name, marks) in student_score.items() if marks >= 60}
print(passed_students)

