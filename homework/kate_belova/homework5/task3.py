students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

s = (
    f'Students {", ".join(students)} '
    f'study these subjects: {", ".join(subjects)}'
)
print(s)
