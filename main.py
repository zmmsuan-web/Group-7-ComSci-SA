def pshs_grade_equivalent(percent):
    if percent >= 96:
         return 1.00, "Excellent"
    elif percent >= 90:
         return 1.25, "Very Good"
    elif percent >= 84: 
         return 1.50, "VERY GOOD"
    elif percent >= 78:
         return 1.75, "GOOD"
    elif percent >= 72:
         return 2.00, "GOOD"
    elif percent >= 66: 
         return 2.25, "SATISFACTORY"
    elif percent >= 60: 
         return 2.50, "SATISFACTORY"
    elif percent >= 55:
         return 2.75, "FAIR"
    elif percent >= 50: 
         return 3.00, "FAIR"
    elif percent >= 40: 
         return 4.00, "FAILED ON CONDITION"
    else: 
         return 5.00, "FAILED"
    
# 1) Input tentative grades (in percent)
tentative_q1_grade = float(input("Enter Tentative Quarter 1 Grade %: "))
tentative_q2_grade = float(input("Enter Tentative Quarter 2 Grade %: "))
tentative_q3_grade = float(input("Enter Tentative Quarter 3 Grade %: "))
tentative_q4_grade = float(input("Enter Tentative Quarter 4 Grade %: "))

# 2) Calculate

# Q1
quarter_1 = tentative_q1_grade

# Q2
quarter_2 = (quarter_1 + 2 * tentative_q2_grade) / 3

# Q3
quarter_3 = (quarter_2 + 2 * tentative_q3_grade) / 3

# Q4 (Final)
quarter_4 = (quarter_3 + 2 * tentative_q4_grade) / 3

# Get equivalent
e, d = pshs_grade_equivalent(quarter_4)

# Output
print("\nResults:")
print("Q1 =", round(quarter_1, 2))
print("Q2 =", round(quarter_2, 2))
print("Q3 =", round(quarter_3, 2))
print("Final Grade =", round(quarter_4, 2))
print("Equivalent =", e, "-", d)

