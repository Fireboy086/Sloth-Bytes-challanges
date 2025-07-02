def lemonade(bills):
    """
    Check if we can provide change for all customers buying lemonade.
    Lemonade costs $5. Customers pay with $5, $10, or $20 bills.
    We start with no money and must provide exact change.
    """
    fives = 0
    tens = 0
    
    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            if fives >= 2:
                fives -= 1
                tens += 1
            else:
                return False
        elif bill == 20:
            # Prefer giving one $10 and one $5 rather than three $5s
            if tens >= 1 and fives >= 1:
                tens -= 1
                fives -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False
    return True

if __name__ == "__main__":
    import tester
    from Cases import LEMONADE_TEST_CASES
    
    tester.run_tests(
        cases=LEMONADE_TEST_CASES,
        test_function=lemonade,
        function_name="lemonade"
    )