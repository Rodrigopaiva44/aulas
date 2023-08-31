# A student score
score = int(input("Score: "))

# operator AND
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 90:
    print("Grade: C")
elif score >= 60 and score < 90:
    print("Grade: D")
else:
    print("Grade: F")

# In Python we can make it better:
if 90 >= score <= 100:
    print("Grade: A")
elif 80 >= score < 90:
    print("Grade: B")
elif 70 >= score < 90:
    print("Grade: C")
elif 60 >= score < 90:
    print("Grade: D")
else:
    print("Grade: F")


# But we can go further

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# At the end, it seems the same because its the same result
# That's why we should remember The Zen of Python (import this)


# Bugs
if score >= 90:
    print("Grade: A")
if score >= 80:
    print("Grade: B")
if score >= 70:
    print("Grade: C")
if score >= 60:
    print("Grade: D")

# Question: We can go even further?
