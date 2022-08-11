"""nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
What was the average temperature in first week of Jan
What was the maximum temperature in first 10 days of Jan
Figure out data structure that is best for this problem"""

# We could use list but it is nowhere written that the data is in sorted order. So we will first create a hash table and then create a sorted array using it.
# Or we can just use a dictionary, but I will use hash table because I am learning it

def hash(string):
    sum = 0
    for char in string:
        sum += ord(char)
    return sum%10

def average(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum/len(arr)

file = open("nyc_weather.txt", 'r')
temp = [[] for _ in range(10)]
templist = [] * 10

for idx, val in enumerate(file):
    val = val.strip()
    h = hash(val.split(",")[0])
    temp[h].append([val.split(",")[0], val.split(",")[1]])

for i in range(1, 11):
    date = "Jan "+str(i)
    h = hash(date)
    for element in temp[h]:
        if element[0] == date:
            templist.append(int(element[1]))

# Answer
print(f"Average in the first week of January: {average(templist[:7])}")
print(f"Maximum in January: {max(templist)}")