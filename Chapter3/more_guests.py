#Exerice 3-6
#Start with your program for 3-5
#Print that you have room for more guests
#Add one at the beginning in the middle and at the end
#Print the new list

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