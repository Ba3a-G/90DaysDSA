"""Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function"""

#Solution
maxNum = input("Please enter a positive integer: ")
oddList = []
try: 
    maxNum = int(maxNum)
    if maxNum < 1:
        raise ValueError

    for i in range(maxNum+1):
        if i%2 == 1:
            oddList.append(i)
    print(oddList)       
except ValueError:
    print("Invalid input")