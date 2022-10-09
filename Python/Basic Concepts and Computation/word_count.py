#Sentences -> input,key ->word, value -> length of the word 
sentence = input("Enter the sentence: ")
words = sentence.split(" ")#split the word according to the spaces 
count_words ={word:len(word) for word in words}
print(count_words)