# elif

score=87

if score >=90:
    grade="A"
elif score >=80:
    grade="B"
elif score >=70:
    grade="c"
elif score >=60:
    grade="D"
else:
    grade="f"
print("For score of % d the grade is %s"%(score,grade))