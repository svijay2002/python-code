import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
marks = [35, 40, 50, 60, 75, 85]

plt.scatter(hours, marks, color="red",
            label="Students")

plt.xlabel("Hours Studied")
plt.ylabel("Exam Marks")
plt.title("Study Hours vs Exam Marks")
plt.legend()
plt.show()