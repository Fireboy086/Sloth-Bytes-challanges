import time

def is_happy_year(year):
    """Check if a year has all unique digits"""
    year_str = str(year)
    return len(year_str) == len(set(year_str))


def next_happy(current):
    """Find the next happy year after the given year"""
    current = int(current) if isinstance(current, str) else current
    year = current 
    while True:
        if is_happy_year(year):
            return year
        year += 1

if __name__ == "__main__":
    import tester
    from Cases import HAPPY_YEAR_TEST_CASES, NEXT_HAPPY_TEST_CASES
    
    print("Testing is_happy_year function:")
    tester.run_tests(
        cases=HAPPY_YEAR_TEST_CASES,
        test_function=is_happy_year,
        function_name="is_happy_year"
    )
    
    print("\nTesting next_happy function:")
    tester.run_tests(
        cases=NEXT_HAPPY_TEST_CASES,
        test_function=next_happy,
        function_name="next_happy",
        timeout=2.0  # Some cases might take a bit longer
    )