def decimalToBinary(number, binary=""):
    if number == 0:
        return int("0"+binary)
    return decimalToBinary(number//2, str(number%2)+binary)

#Driver code
"""if __name__ == "__main__":
    print(f"I convert decimal to binary, for example 13 is {decimalToBinary(13)}.")"""

print(decimalToBinary(39))