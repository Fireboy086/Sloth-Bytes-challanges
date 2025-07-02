def digits(n: int):
    """Count total number of digits used to write all numbers from 1 to n-1"""
    out = 0
    for i in range(1, n):
        out += len(str(i))
    return out

if __name__ == "__main__":
    import tester
    from Cases import NDIGITS_TEST_CASES
    
    tester.run_tests(
        cases=NDIGITS_TEST_CASES,
        test_function=digits,
        function_name="digits"
    )