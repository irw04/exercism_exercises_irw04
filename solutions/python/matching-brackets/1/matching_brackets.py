def is_paired(input_string):
    bracket_dict = {"(":")", "{":"}","[":"]"}
    match = []

    for char in input_string:
        if char in bracket_dict.keys():
            match.append(char)
        elif char in bracket_dict.values():
            if not match or bracket_dict[match.pop()] != char:
                return False

    return len(match) == 0


    """def is_paired(input_string):
    bracket_dict = {"(":")", "{":"}","[":"]"}
    match = []
    for char in input_string:
        if char in bracket_dict.values():
            match.append(char)
        elif char in bracket_dict.keys:
            if not match or match.pop() != bracket_dict[char]:
                return False
    return len(match) == 0 """