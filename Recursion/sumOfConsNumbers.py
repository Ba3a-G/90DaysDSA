info = "There are multiple ways of doing this. I would prefer the mathematical option because of its simplicity and speed."

def sumRecursion(number, sum=0):
    if number <= 0:
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
    import argparse
    parser = argparse.ArgumentParser(description="Gives the sum of the given first N natural numbers.",
        usage="python sumOfConsNumbers.py 'N'")
    parser.add_argument("N", type=int)
    args = parser.parse_args()

    print(sumRecursion(args.N))
