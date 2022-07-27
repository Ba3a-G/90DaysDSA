info = "There are multiple ways of doing this. I would prefer the mathematical option because of its simplicity and speed."

def sumRecursion(number, sum=0):
    if number == 0:
        return sum
    return (sumRecursion(number-1, sum+number))

def sumMath(number):
    return number*(number+1)/2

def sumIterate(number):
    sum = 0
    for n in range(1, number+1):
        sum+=n
    return sum

if __name__ == "__main__":
    print(f"I return the sum of given first N natural numbers, for example, the sum of first 6 natural numbers is {sumRecursion(6)}. \n{info}")