def convert_to_title(n):
    if n <= 0:
        return ""
    
    result = ""
    while n > 0:
        n -= 1  # Excel columns are 1-indexed, not 0-indexed
        result = chr(65 + (n % 26)) + result  # 65 is ASCII for 'A'
        n //= 26
    
    return result

# Test cases
tests = [
    (1, "A"),
    (18, "R"),
    (28, "AB"),
    (52, "AZ"),
    (701, "ZY"),
    (229704, "MATT"),
    (209380622941, "ZATOICHI"),
    # Edge cases
    (26, "Z"),
    (27, "AA"),
    (702, "ZZ"),
    (703, "AAA"),
    (18278, "ZZZ"),
    (18279, "AAAA"),
    # Some medium-sized numbers
    (100, "CV"),
    (500, "SF"),
    (1000, "ALL"),
    (5000, "GJH"),
    # Large numbers
    (1000000, "BDWGN"),
    (999999999, "CFDGSXK"),
]

print("\033[1m\033[94m#=====================#======-TESTS-=======#====================#\033[0m")
passed = 0
failed = 0
for number, expected in tests:
    result = convert_to_title(number)
    if result == expected:
        print(f"\033[1m\033[92m{(f'PASS: convert_to_title({number}) == {expected}'):^65}\033[0m")
        passed += 1
    else:
        print(f"\033[91m{(f'FAIL: convert_to_title({number}) == {result} (expected {expected})'):^65}\033[0m")
        failed += 1
print(f"\033[94m{('#===========#======-SUMMARY-=======#===========#'):^65}\033[0m")
print(f"\033[1m\033[35m{(str(passed) + ' passed, ' + str(failed) + ' failed'):^65}\033[0m")
