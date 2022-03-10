import random
import pandas

# new_dict = { new_key:new_value for (key, value) item in dict.items() }

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# student_score = {name: random.randint(50, 99) for name in names}
student_score = {'Alex': 88, 'Beth': 83, 'Caroline': 71, 'Dave': 50, 'Eleanor': 86, 'Freddie': 61}

print(student_score)

passed_students = {name: marks for (name, marks) in student_score.items() if marks >= 60}
print(passed_students)

students_marks = {
    "student": names,
    "score": [88, 93, 33, 80, 92, 59]
}

student_score_dataframe = pandas.DataFrame(students_marks)
for (index, row) in student_score_dataframe.iterrows():
    if row.student == "Alex":
        print(row.score)

phonetic_dict = pandas.read_csv('./nato_phonetic_alphabet.csv')
print(phonetic_dict)

user_input = input("Enter the word to convert to phonetic Nato\n")
# phonetic_converted_code = []
# for character in user_input.lower():
#     output_result = {character: row.code for (index, row) in phonetic_dict.iterrows() if
#                      character in row.letter.lower()}
#     phonetic_converted_code.append(output_result)

# print(phonetic_converted_code)
print([{character: row.code for (index, row) in phonetic_dict.iterrows() if character in row.letter.lower()}
      for character in user_input.lower()])

