finalString = ""
special=[" ", ",", ".", "?"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

stringOtext = str(input("What is your string you need to translate? "))
stringOtext = stringOtext.upper()

for char in stringOtext:
    if char in special:
        if char == " ":
            finalString += " "
        elif char == ",":
            finalString += "--..--"
        elif char == ".":
            finalString += ".-.-.-"
        else:
            finalString += "..--.."
    if char in numbers:
        if char == "0":
            finalString += "-----"
        elif char == "1":
            finalString += ".----"
        elif char == "2":
            finalString += "..---"
        elif char == "3":
            finalString += "...--"
        elif char == "4":
            finalString += "....-"
        elif char == "5":
            finalString += "....."
        elif char == "6":
            finalString += "-...."
        elif char == "7":
            finalString += "--..."
        elif char == "8":
            finalString += "---.."
        else:
            finalString += "----."
    if char in letters:
        if char == "A":
            finalString += ".-"
        elif char == "B":
            finalString += "-..."
        elif char == "C":
            finalString += "-.-."
        elif char == "D":
            finalString += "-.."
        elif char == "E":
            finalString += "."
        elif char == "F":
            finalString += "..-."
        elif char == "G":
            finalString += "--."
        elif char == "H":
            finalString += "...."
        elif char == "I":
            finalString += ".."
        elif char == "J":
            finalString += ".---"
        elif char == "K":
            finalString += "-.-"
        elif char == "L":
            finalString += ".-.."
        elif char == "M":
            finalString += "--"
        elif char == "N":
            finalString += "-."
        elif char == "O":
            finalString += "---"
        elif char == "P":
            finalString += ".--."
        elif char == "Q":
            finalString += "--.-"
        elif char == "R":
            finalString += ".-."
        elif char == "S":
            finalString += "..."
        elif char == "T":
            finalString += "-"
        elif char == "U":
            finalString += "..-"
        elif char == "V":
            finalString += "...-"
        elif char == "W":
            finalString += ".--"
        elif char == "X":
            finalString += "-..-"
        elif char == "Y":
            finalString += "-.--"
        else:
            finalString += "--.."
    if char != " ":
        finalString += " "
print(finalString)