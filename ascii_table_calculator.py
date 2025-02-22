while(True):
    s = input("\n> ")
    match len(s):
        case 1:
            print(f"{s}: {ord(s)}")
        case 2: 
            print(f"{s[0]} to {s[1]}: {ord(s[1]) - ord(s[0])}")
        case _:
            print("no output")
