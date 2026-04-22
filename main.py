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

quarter_1 = tentative_q1_grade
