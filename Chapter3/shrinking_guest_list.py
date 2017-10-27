#Exerice 3-7
#Start with your program for 3-6
#Print that you only have room for two guests
#pop until you only have two guests
#Print the new list
#use del to empty the list
#print to make sure you have an empty list

inviting = ["Denzel Washington", "Emma Stone", "Amy Adams"]
print(inviting[0] + " Would you come to my dinner party")
print(inviting[1] + " Would you come to my dinner party")
print(inviting[2] + " Would you come to my dinner party")
print("\n")

print(inviting[0] + " can't attend")
inviting[0] = "Emily Blunt"
print(inviting[0] + " Would you come to my dinner party")
print(inviting[1] + " Would you come to my dinner party")
print(inviting[2] + " Would you come to my dinner party")
print("\n")

print("I have more room!")
inviting.insert(0,"Tom Hanks")
inviting.insert(2,"David Simmon")
inviting.append("Charlie Kaufman")
print(inviting[0] + " Would you come to my dinner party")
print(inviting[1] + " Would you come to my dinner party")
print(inviting[2] + " Would you come to my dinner party")
print(inviting[3] + " Would you come to my dinner party")
print(inviting[4] + " Would you come to my dinner party")
print(inviting[5] + " Would you come to my dinner party")
print("\n")

inviting.pop(0)
inviting.pop(0)
inviting.pop(0)
inviting.pop()
print(inviting[0] + " Would you come to my dinner party")
print(inviting[1] + " Would you come to my dinner party")
del inviting[0]
del inviting[0]
print(inviting)