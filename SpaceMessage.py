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

print(spaceMessage("[1000WOW]"))
print(spaceMessage("IF[2E]LG[5O]D"))
print(spaceMessage("AB[3CD]"))
print(spaceMessage("ABCD"))
print(spaceMessage(""))



#           _______  _______  _        _______      _______  _        _______           _        _______  _______  _______  _
# |\     /|(  ___  )(  ____ )| \    /\(  ____ \    (  ____ \( \      (  ___  )|\     /|( \      (  ____ \(  ____ \(  ____ \( \   |\     /|
# | )   ( || (   ) || (    )||  \  / /| (    \/    | (    \/| (      | (   ) || )   ( || (      | (    \/| (    \/| (    \/| (   ( \   / )
# | | _ | || |   | || (____)||  (_/ / | (_____     | (__    | |      | (___) || | _ | || |      | (__    | (_____ | (_____ | |    \ (_) /
# | |( )| || |   | ||     __)|   _ (  (_____  )    |  __)   | |      |  ___  || |( )| || |      |  __)   (_____  )(_____  )| |     \   /
# | || || || |   | || (\ (   |  ( \ \       ) |    | (      | |      | (   ) || || || || |      | (            ) |      ) || |      ) (
# | () () || (___) || ) \ \__|  /  \ \/\____) |    | )      | (____/\| )   ( || () () || (____/\| (____/\/\____) |/\____) || (____/\| |
# (_______)(_______)|/   \__/|_/    \/\_______)    |/       (_______/|/     \|(_______)(_______/(_______/\_______)\_______)(_______/\_/
