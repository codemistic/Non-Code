#A recent survey has been made on the people reading various newspapers. 
# Based on the survey, some group of people reading 
# „The Hindu‟ and/or „Indian Express‟ have been considered. 
# Assume cluster A is reading „The Hindu‟ 
# and cluster B is reading „Indian Express‟. 
# Use a suitable sequence data type to compute the following task such as: 
#  People reading both the newspapers 
#  People reading either of newspapers 
#  People reading only „The Hindu‟, but not „Indian Express‟ 
#  People reading only „Indian Express‟, but not „The Hindu‟ 
# Sample Input: 
# Cluster A: {Aarthi, Lavanya, Rekha, Praveen, Sankar, Sai, Nirmal, Vignesh} 
# Cluster B :{ Lavanya, Praveen, Priyanka, Janani, Nirmal, Karthik, Kishore, Gopi} 
# sample output: 
# (i) People reading both the newspapers are 
#  Lavanya 
# Praveen 
# Nirmal

print("Enter the names of people who read The Hindu :")
Cluster_A = set()
while True :
    x = input()
    Cluster_A.add(x)

    if not x:
        break


print("Enter the names of people who read Indian Express :")
Cluster_B = set()
while True :
    x = input()
    Cluster_B.add(x)

    if not x:
        break

print("\n\n")   

#People reading both the newspaper 
print("People reading both the newspapers are :")
A = Cluster_A&Cluster_B
for i in A:
    print(i)


print("\n\n")

#People reading either of the newspaper 
print("People reading either of the newspapers are :")
A = Cluster_A|Cluster_B
for i in A:
    print(i)

print("\n\n")

#People reading both The Hindu but not Indian Express
print("People reading The Hindu but not THe Indian Express are :")
A = Cluster_A-Cluster_B
for i in A:
    print(i)

print("\n\n")

#People reading The Indian Express but not The Hindu
print("People reading The Indian Express but not The Hindu :")
A = Cluster_B-Cluster_A
for i in A:
    print(i)




