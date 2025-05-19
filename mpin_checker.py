
def is_common_mpin(mpin, common_mpin_list=None):
    if common_mpin_list is None:
        common_mpin_list = ['1234', '0000', '1111', '1122', '1212', '4321', 
                            '2222', '9999', '2580', '5555', '123456', '654321', '111111', '000000']
    return mpin in common_mpin_list

def generate_date_variants(date):
    if not date:
        return set()
    dd, mm, yyyy = date.split('-')
    yy = yyyy[-2:]
    return {
        dd + mm, mm + dd, yy + mm, mm + yy,
        yy + dd, dd + yy, yyyy, yy
    }

def check_mpin_strength(mpin, dob=None, anniversary=None, spouse_dob=None):
    reasons = []

    # Check commonly used MPINs
    if is_common_mpin(mpin):
        reasons.append("COMMONLY_USED")

    # Check demographic patterns
    if dob and mpin in generate_date_variants(dob):
        reasons.append("DEMOGRAPHIC_DOB_SELF")
    if spouse_dob and mpin in generate_date_variants(spouse_dob):
        reasons.append("DEMOGRAPHIC_DOB_SPOUSE")
    if anniversary and mpin in generate_date_variants(anniversary):
        reasons.append("DEMOGRAPHIC_ANNIVERSARY")

    strength = "WEAK" if reasons else "STRONG"
    return strength, reasons

def main():
    print("Welcome to MPIN Strength Checker!")
    mpin = input("Enter your MPIN (4 or 6 digits): ").strip()
    dob = input("Enter your Date of Birth (DD-MM-YYYY) or press Enter to skip: ").strip()
    anniversary = input("Enter your Wedding Anniversary (DD-MM-YYYY) or press Enter to skip: ").strip()
    spouse_dob = input("Enter your Spouse's Date of Birth (DD-MM-YYYY) or press Enter to skip: ").strip()

    strength, reasons = check_mpin_strength(mpin, dob, anniversary, spouse_dob)

    print(f"\nMPIN Strength: {strength}")
    if reasons:
        print("Reasons for Weak MPIN:")
        for reason in reasons:
            print(f"- {reason}")
    else:
        print("Your MPIN is strong!")

# Test cases
def run_tests():
    test_cases = [
        # Common MPINs
        ("1234", None, None, None, "WEAK", ["COMMONLY_USED"]),
        ("0000", None, None, None, "WEAK", ["COMMONLY_USED"]),
        ("2580", None, None, None, "WEAK", ["COMMONLY_USED"]),
        ("4321", None, None, None, "WEAK", ["COMMONLY_USED"]),
        # Demographic DOB Self
        ("0201", "02-01-1998", None, None, "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
        ("9802", "02-01-1998", None, None, "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
        ("1998", "02-01-1998", None, None, "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
        # Demographic DOB Spouse
        ("1503", None, None, "15-03-1990", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
        ("0315", None, None, "15-03-1990", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
        # Demographic Anniversary
        ("2507", None, "25-07-2010", None, "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
        ("0725", None, "25-07-2010", None, "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
        # Strong MPINs
        ("7890", None, None, None, "STRONG", []),
        ("5678", "02-01-1998", "25-07-2010", "15-03-1990", "STRONG", []),
        # 6-digit MPINs
        ("123456", None, None, None, "WEAK", ["COMMONLY_USED"]),
        ("020198", "02-01-1998", None, None, "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
        ("150390", None, None, "15-03-1990", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
        ("250710", None, "25-07-2010", None, "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
        ("654321", None, None, None, "WEAK", ["COMMONLY_USED"]),
        ("789012", None, None, None, "STRONG", []),
    ]

    for i, (mpin, dob, anniversary, spouse_dob, expected_strength, expected_reasons) in enumerate(test_cases, 1):
        strength, reasons = check_mpin_strength(mpin, dob, anniversary, spouse_dob)
        assert strength == expected_strength, f"Test case {i} failed: Expected strength {expected_strength}, got {strength}"
        assert reasons == expected_reasons, f"Test case {i} failed: Expected reasons {expected_reasons}, got {reasons}"
        print(f"Test case {i} passed.")

if __name__ == "__main__":
    # Uncomment the following line to run tests
    # run_tests()
    main()
