

students = [
    ("Ana", 18.5), ("Luis", 16.0),
    ("Maria", 19.2), ("Pedro", 15.7),
    ("Sofia", 18.5)
]

top3 = []

for name, grade in students:
    position = 0

    while position < len(top3) and grade <= top3[position][1]:
        position += 1 
    top3.insert(position, (name, grade))
    if len(top3) > 3:
        top3.pop()

print("TOP 3 STUDENTS")

for name, grade in top3:
    print(name, grade)
