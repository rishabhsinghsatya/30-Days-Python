student = {"name": "John", "age": 32, "courses": ["javascript", "python"]}

# accessing value
print(student)  # {'name': 'John', 'age': 32, 'courses': ['javascript', 'python']}
print(student["name"])  # john
print(student["courses"])  # ['javascript', 'python']
print(student["courses"][0])  # javascript

# adding
student["grade"] = "A"

# updating
student["age"] = 22
print(student)

# removing
del student["grade"]

print(student)

# iterate dictionary over keys
for key in student:
    print(key)

# iterate dictionary over values
for value in student.values():
    print(value)

# iterate over key:value pair
for key, value in student.items():
    print(f"{key}:{value}")


# ----------merge 2 lists into a dictionary---------- #

keys = ["john", "jack", "adam"]
values = ["python", "java", "javascript"]

data = dict(zip(keys, values))
print(data)  # {'john': 'python', 'jack': 'java', 'adam': 'javascript'}

data["alvin"] = "golang"
print(data) # {'john': 'python', 'jack': 'java', 'adam': 'javascript', 'alvin': 'golang'}