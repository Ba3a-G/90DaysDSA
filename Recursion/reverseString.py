def reverseString(string):
    if len(string) == 0:
        return ""
    return reverseString(string[1:]) + string[0]

def reverseStringAlter(string):
    n = len(string)
    if n==0:
        return ""
    return string[n-1] + reverseStringAlter(string[0:n-1])

#Driver code
if __name__ == "__main__":
    print("I can reverse strings. " + reverseString("Like this!"))