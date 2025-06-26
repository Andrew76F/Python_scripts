wordFreq = {} #creates empty dictionary

filename = input("Please input your filepath(REMOVE QUOTATION MARKS FROM FILEPATH): ") #input your file path, REMOVE QUOTATION MARKS FROM PATH
file = open(filename, "r") #opens the .txt
text = (file.read()) #reads the contents of word frequency.txt and saves it to a variable named text
x = text.split() #takes the text variable and preforms .split which separates each word into an iterable list
for word in x: #loop to loop through the list of words
    if word in wordFreq: #if the word/key is already in the dictionary.....
        wordFreq[word] += 1 #change the value by +1
    else: #if the word IS NOT in the dictionary......
        wordFreq[word] = 1 #add the key and make the value 1
print(*wordFreq.items()) #print out the full list of items in the dictionary.
file.close()# and finally close the file, honestly could've been done 7 lines ago....