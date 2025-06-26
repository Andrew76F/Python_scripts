import re
trash = []
challenge_string = "2 Happy 60 To End 7 This 8 Semester 54"
challenge_list = re.split(r'\s', challenge_string)
length = len(challenge_list)
for i in range(0,length):
    if re.search(r'[a-zA-Z]', challenge_list[i]):
        trash.append(challenge_list[i])

numList = []
for i in range(0,length):
    if challenge_list[i-1] not in trash:
        numList.append(challenge_list[i-1])
numList2 = []
for i in numList:
    numList2.append(int(i))
print(numList2)
numList2.sort()
numList2.reverse()
print(numList2)