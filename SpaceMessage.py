def unfold_brackets(string):
    # Lists to store characters and numbers separately
    out = []
    mult = []
    for s in string:
        if not s.isdigit():
            out.append(s)
        else:
            mult.append(s)
    # Multiply the letters by the number
    outstr = int("".join(mult)) * "".join(out)
    return outstr

def spaceMessage(init):
    """
    Decode a space message by expanding bracketed expressions.
    Format: [NumberLetters] expands to Letters repeated Number times.
    """
    # Lists to store temporary chars and final result
    temp_brackets = []
    out_no_brackets = []
    inbrackets = False

    for s in init:
        if s == "[":
            inbrackets = True
        elif s == "]":
            inbrackets = False
            # Process what was inside brackets
            out_no_brackets.append(unfold_brackets("".join(temp_brackets)))
            temp_brackets.clear()
        else:
            if not inbrackets:
                out_no_brackets.append(s)
            if inbrackets:
                temp_brackets.append(s)
    return "".join(out_no_brackets)

if __name__ == "__main__":
    import tester
    from Cases import SPACE_MESSAGE_TEST_CASES
    
    tester.run_tests(
        cases=SPACE_MESSAGE_TEST_CASES,
        test_function=spaceMessage,
        function_name="spaceMessage"
    )


#           _______  _______  _        _______      _______  _        _______           _        _______  _______  _______  _
# |\     /|(  ___  )(  ____ )| \    /\(  ____ \    (  ____ \( \      (  ___  )|\     /|( \      (  ____ \(  ____ \(  ____ \( \   |\     /|
# | )   ( || (   ) || (    )||  \  / /| (    \/    | (    \/| (      | (   ) || )   ( || (      | (    \/| (    \/| (    \/| (   ( \   / )
# | | _ | || |   | || (____)||  (_/ / | (_____     | (__    | |      | (___) || | _ | || |      | (__    | (_____ | (_____ | |    \ (_) /
# | |( )| || |   | ||     __)|   _ (  (_____  )    |  __)   | |      |  ___  || |( )| || |      |  __)   (_____  )(_____  )| |     \   /
# | || || || |   | || (\ (   |  ( \ \       ) |    | (      | |      | (   ) || || || || |      | (            ) |      ) || |      ) (
# | () () || (___) || ) \ \__|  /  \ \/\____) |    | )      | (____/\| )   ( || () () || (____/\| (____/\/\____) |/\____) || (____/\| |
# (_______)(_______)|/   \__/|_/    \/\_______)    |/       (_______/|/     \|(_______)(_______/(_______/\_______)\_______)(_______/\_/
