def digitsSimple(n: int):
    """Count total number of digits used to write all numbers from 1 to n-1"""
    out = 0
    for i in range(1, n):
        out += len(str(i))
    return out

def digits(n: int):
    """Count total number of digits used to write all numbers from 1 to n-1"""
    numDigits = len(str(n-1))
    rest = n
    out=0
    if numDigits == 1:
        return n-1
    else:
        for i in range(numDigits,0,-1):
            sub =(rest-10**(numDigits-1))
            out += sub *numDigits
            rest -= sub
            numDigits -= 1
    return out



if __name__ == "__main__":
    import tester
    from Cases import NDIGITS_TEST_CASES
    
    tester.run_tests(
        cases=NDIGITS_TEST_CASES,
        numChecks=-1,
        test_function=digits,
        function_name="digits"
    )