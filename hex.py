def is_valid_hex_code(hex_code):
    if hex_code[0] != "#":
        return False
    if len(hex_code) != 7:
        return False
    for char in hex_code[1:].lower():
        if (
            ord(char) not in range(61, 103) and # a-f
            ord(char) not in range(48, 58)      # 0-9
        ):
            return False
    return True


tests = [
    ("#CD5C5C", True),
    ("#EAECEF", True),
    ("#eaec09", True),
    ("#CD5C58C", False),  # Length exceeds 6
    ("#CD5C5Z", False),   # Not all alphabetic characters in A-F
    ("#CD5C&C", False),   # Contains unacceptable character
    ("CD5C5C", False),    # Missing #
]

for code, expected in tests:
    result = is_valid_hex_code(code)
    if result == expected:
        print(f"\033[92mPASS: is_valid_hex_code({code!r}) == {expected}\033[0m")
    else:
        print(f"\033[91mFAIL: is_valid_hex_code({code!r}) == {result} (expected {expected})\033[0m")
