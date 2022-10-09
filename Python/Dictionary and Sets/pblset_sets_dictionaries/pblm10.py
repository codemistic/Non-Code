#sort words in a sentence in decreasing order of their length. 
# Display the sorted words along with their length

n = input("Enter the sentence :")
l = []
words = n.split()
for word in words:
    l.append(words)

dict_word = {}
for i in range(0,len(l)):
    
    c = l[i][i]
    dict_word.update({c:len(c)})

print(sorted(dict_word.items(), key=lambda x: x[1::-1]))