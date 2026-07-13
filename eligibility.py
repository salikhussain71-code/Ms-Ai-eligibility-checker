# eligibility.py
# MS AI Program Eligibility Checker
# Checks eligibility for MBZUAI, KAUST, and LUMS
# CS50P Week 3 Project

from exceptions import InvalidScoreError

def get_float(prompt):
    """Get a float from user with error handling."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_mbzuai(cgpa, ielts, gre):
    """Check eligibility for MBZUAI. Source: mbzuai.ac.ae"""
    # MBZUAI Min: CGPA 3.2/4.0, IELTS 6.5, GRE 300 recommended
    if cgpa >= 3.2 and ielts >= 6.5 and gre >= 300:
        return "Eligible", "Meets all minimum requirements"
    else:
        reason = []
        if cgpa < 3.2:
            reason.append(f"CGPA below 3.2")
        if ielts < 6.5:
            reason.append(f"IELTS below 6.5")
        if gre < 300:
            reason.append(f"GRE below 300")
        return "Not Eligible", ", ".join(reason)

def check_kaust(cgpa, ielts, gre):
    """Check eligibility for KAUST. Source: kaust.edu.sa"""
    # KAUST Min: CGPA 3.5/4.0, IELTS 6.5, GRE 315 recommended
    if cgpa >= 3.5 and ielts >= 6.5 and gre >= 315:
        return "Eligible", "Meets all minimum requirements"
    else:
        reason = []
        if cgpa < 3.5:
            reason.append(f"CGPA below 3.5")
        if ielts < 6.5:
            reason.append(f"IELTS below 6.5")
        if gre < 315:
            reason.append(f"GRE below 315")
        return "Not Eligible", ", ".join(reason)

def check_lums(cgpa, ielts, gre):
    """Check eligibility for LUMS. Source: lums.edu.pk"""
    # LUMS SDSB Min: CGPA 2.5/4.0, IELTS 6.0, GRE not mandatory but 300+ preferred
    if cgpa >= 2.5 and ielts >= 6.0:
        if gre >= 300:
            return "Eligible", "Strong profile"
        else:
            return "Check Requirements", "GRE below 300 but other criteria met"
    else:
        reason = []
        if cgpa < 2.5:
            reason.append(f"CGPA below 2.5")
        if ielts < 6.0:
            reason.append(f"IELTS below 6.0")
        return "Not Eligible", ", ".join(reason)

def main():
    print("=" * 50)
    print("  MS AI PROGRAM ELIGIBILITY CHECKER")
    print("=" * 50)
    
    # Get input
    cgpa = get_float("Enter your CGPA (out of 4.0): ")
    ielts = get_float("Enter your IELTS score (out of 9.0): ")
    gre = get_float("Enter your GRE score: ")
    
    # Validate using custom exception
    if cgpa < 0 or cgpa > 4.0:
        raise InvalidScoreError(f"CGPA must be between 0.0 and 4.0. You entered {cgpa}")
    if ielts < 0 or ielts > 9.0:
        raise InvalidScoreError(f"IELTS must be between 0.0 and 9.0. You entered {ielts}")
    
    print("\n" + "-" * 50)
    print(f"{'University':<15} {'Status':<18} {'Reason'}")
    print("-" * 50)
    
    # Check each university
    for name, func in [("MBZUAI", check_mbzuai), ("KAUST", check_kaust), ("LUMS", check_lums)]:
        status, reason = func(cgpa, ielts, gre)
        print(f"{name:<15} {status:<18} {reason}")
    
    print("-" * 50)

if __name__ == "__main__":
    main()