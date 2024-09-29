import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!

def match_pattern(input_line, pattern):
    print(f"Current input_line: [{input_line}]")
    print(f"Current pattern: [{pattern}]")
    print("")

    # Base cases
    if not pattern: 
        print("Hit!")
        return True
    if not input_line: return False
    
    # Matching a singular character
    if pattern[0] == input_line[0]: 
        return match_pattern(input_line[1:], pattern[1:])

    # Match digit or alphanum
    if pattern[0] == '\\':
        if pattern[1] == 'w' and input_line[0].isalnum():
            return match_pattern(input_line[1:], pattern[2:])
        if pattern[1] == 'd' and input_line[0].isdigit():
            return match_pattern(input_line[1:], pattern[2:])

    # Match group
    if pattern[0] == '[' and pattern[-1] == ']':
        if pattern[1] == '^':
            return not any(c in pattern[2:-1] for c in input_line)
        return any(c in pattern[1:-1] for c in input_line)

    # Nothing found
    print("L")
    return False

def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # Anchors happen here
    if pattern[0] == '^':
        exit(0) if match_pattern(input_line, pattern[1:]) else exit(1)
    elif any(match_pattern(input_line[i:], pattern) for i in range(len(input_line))):
        exit(0)
    print("massive L")
    exit(1)


if __name__ == "__main__":
    main()
