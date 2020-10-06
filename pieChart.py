import matplotlib.pyplot as plt
subjects = ["maths" , "english", "physics", "chemistry", "PEd"]
marks = [95,83,83,94,95]

plt.pie(marks , labels=subjects, shadow=True)
plt.title("12th Board result")
plt.show()