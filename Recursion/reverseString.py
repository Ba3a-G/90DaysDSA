def reverseString(string):
    if len(string) == 0:
        return ""
    return reverseString(string[1:]) + string[0]

def reverseStringAlter(string):
    if len(string)==0:
        return ""
    return string[-1] + reverseStringAlter(string[0:-1])



#Driver code
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Reverses the given string.",
        usage="python reverseString.py 'your string'")
    parser.add_argument("string", type=str)
    args = parser.parse_args()

    print(reverseString(args.string))