last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

# Initialize gradebook
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

print(gradebook)

# Add new content
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
print(gradebook)

# Update existing content
gradebook[5][1] += 5
gradebook[2].remove(85)
gradebook[2].append("Pass")

# Combine two contents
full_grade_book = last_semester_gradebook + gradebook
print(full_grade_book)

