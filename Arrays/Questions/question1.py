"""Question: You have a list of your favourite marvel super heros.
heroes=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)"""

#Solution
heroes = ['spider man','thor','hulk','iron man','captain america']

length = len(heroes)

heroes.append("black panther")

indexOfHulk=0
for hero in heroes:
    if hero == "hulk":
        heroes.remove("black panther")
        heroes.insert(indexOfHulk+1, "black panther")
        print(heroes)
        break
    indexOfHulk+=1

pointer = 0
for i in heroes:
    if i == "hulk":
        indexHulk = pointer
    if i == "thor":
        indexThor = pointer
    pointer+=1
#Assuming Thor and Hulk are adjacent
if indexHulk < indexThor:
    heroes[indexHulk : indexThor+1] = ["dr strange"]
else:
    heroes[indexThor : indexHulk+1] = ["dr strange"]

heroes.sort()