# loan eligibility 

def check_loan_eligibility(age, cibil_score, income, loan_amount, loan_term, employment_type):
    if age < 21 or age > 60:
        return "❌ Not eligible: Age must be between 21 and 60."
    if cibil_score < 650:
        return "❌ Not eligible: Low CIBIL score."
    if income < 15000:
        return "❌ Not eligible: Income too low."
    if employment_type.lower() not in ['salaried', 'self-employed']:
        return "❌ Not eligible: Invalid employment type."
    
    # Simple loan EMI check (max 40% of income allowed)
    monthly_emi = loan_amount / (loan_term * 12)
    if monthly_emi > (income * 0.4):
        return "❌ Not eligible: EMI too high for your income."

    return "✅ Eligible for loan."

# Input from user

age = int(input("Enter your age: "))
cibil = int(input("Enter your CIBIL score: "))
income = int(input("Enter your monthly income (₹): "))
loan_amount = int(input("Enter desired loan amount (₹): "))
loan_term = int(input("Enter loan term (in years): "))
employment = input("Enter employment type (salaried/self-employed): ")

# Result
result = check_loan_eligibility(age, cibil, income, loan_amount, loan_term, employment)
print(result)
