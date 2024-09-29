import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!

def testing(input_line, pattern):
    # Base cases
    if not pattern: return True
    if not input_line: return False
    # Matching a singular character
    if pattern[0] == input_line: testing(input_line[1:], pattern[1:])
    # Match digit or alphanum
    if pattern[0] == '\\':
        if pattern[1] == 'w' and input_line[0].isalnum():
            testing(input_line[1], pattern[2:])
        if pattern[1] == 'd' and input_line[0].isdigit():
            testing(input_line[1], pattern[2:])
    #Match group
    if pattern[0] == '[':
        opposite, i, group = 1, 1, set()
        if pattern[1] == '^': 
            i, opposite = 2, 0
        while pattern[i] != ']':
            group.add(pattern[i])
        if input_line[0] in group == opposite:
            testing(input_line[1:], pattern[i:])
        else:
            return False
    testing(input_line[1:], pattern)

#def match_pattern(input_line, pattern):
#    if len(pattern) == 1:
#        return pattern in input_line
#    elif pattern == "\\d":
#        return any(c.isdigit() for c in input_line)
#    elif pattern == "\\w":
#        return any(c.isalnum() for c in input_line)
#    elif pattern[0] == '[' and pattern[-1] == ']':
#        if pattern[1] == '^':
#            return not any(c in pattern[2:-1] for c in input_line)
#        return any(c in pattern[1:-1] for c in input_line)
#
#    return pattern in input_line


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    #print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    if testing(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
