import pandas as pd

# Load CSV file
df = pd.read_csv("students.csv")

print("\n----- STUDENT DATA -----")
print(df)

# Cleaning data
df = df.dropna()

# Average marks
average_marks = df["Marks"].mean()

print("\nAverage Marks:", average_marks)

# Highest marks
highest_marks = df["Marks"].max()

print("Highest Marks:", highest_marks)

# Filter top students
top_students = df[df["Marks"] > 80]

print("\n----- TOP STUDENTS -----")
print(top_students)

# Group by department
department_average = df.groupby("Department")["Marks"].mean()

print("\n----- DEPARTMENT AVERAGE -----")
print(department_average)