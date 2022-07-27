def isPalindrome(string):
    n = len(string)
    string = string.lower()
    if n<2:
        return True
    if string[0] == string[n-1]:
        return isPalindrome(string[1:n-1])
    else:
        return False

#Driver code
if __name__ == "__main__":
    print("I can check if a string is a palindrome.")
    print("Is 'kayak' a palindrome: " + str(isPalindrome("kayak")))
    print("Is 'banana' a palindrome: " + str(isPalindrome("banana")))