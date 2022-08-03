def isPalindrome(string):
    n = len(string)
    string = string.lower()
    if n<2:
        return True
    return isPalindrome(string[1:n-1]) if string[0] == string[n-1] else False

def isPalindromeAliter(string):
    mid = len(string)//2
    left = string[0:mid]
    right = ""
    for i in range(1,mid+1):
        right += string[-i]
    return True if left == right else False

#Driver code
if __name__ == "__main__":
    print("I can check if a string is a palindrome.")
    print("Is 'kayak' a palindrome: " + str(isPalindrome("kayak")))
    print("Is 'banana' a palindrome: " + str(isPalindrome("banana")))