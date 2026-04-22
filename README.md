def get_pshs_equivalence(percent):
# Returns (Numerical Equivalent, Adjectival Equivalent)
    if percent >= 96: return 1.00, "EXCELLENT"
    elif percent >= 90: return 1.25, "VERY GOOD"
    elif percent >= 84: return 1.50, "VERY GOOD"
    elif percent >= 78: return 1.75, "GOOD"
    elif percent >= 72: return 2.00, "GOOD"
    elif percent >= 66: return 2.25, "SATISFACTORY"
    elif percent >= 60: return 2.50, "SATISFACTORY"
    elif percent >= 55: return 2.75, "FAIR"
    elif percent >= 50: return 3.00, "FAIR"
    elif percent >= 40: return 4.00, "FAILED ON CONDITION"
    else: return 5.00, "FAILED"

# 1. Input tentative percentage grades
tq1 = float(input("Enter Tentative Q1 Grade (%): "))
tq2 = float(input("Enter Tentative Q2 Grade (%): "))
tq3 = float(input("Enter Tentative Q3 Grade (%): "))
tq4 = float(input("Enter Tentative Q4 Grade (%): "))

# 2. Sequential cumulative calculation
q1 = tq1
q2 = (q1 + 2 * tq2) / 3
q3 = (q2 + 2 * tq3) / 3
q4 = (q3 + 2 * tq4) / 3  # Final Grade1

# 3. Get official equivalents for the Final Grade
num_equiv, adj_equiv = get_pshs_equivalence(q4)

# 4. Display Results
print("\n" + "="*40)
print(f"{'PSHS QUARTERLY REPORT':^40}")
print("="*40)
print(f"Q1 Performance: {q1:>10.2f}%")
print(f"Q2 Performance: {q2:>10.2f}%")
print(f"Q3 Performance: {q3:>10.2f}%")
print("-" * 40)
print(f"FINAL PERCENTAGE: {q4:>10.2f}%")
print(f"NUMERICAL GRADE:  {num_equiv:>10.2f}")
print(f"ADJECTIVAL:       {adj_equiv:>10}")
print("="*40)
