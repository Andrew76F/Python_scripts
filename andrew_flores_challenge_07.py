def main():
    getUserPass()
    
def getUserPass():
    userName = str(input("Create a username "))
    password = str(input("Create a password "))
    print(storedPasswords(password)) 
    
def storedPasswords(checkPass):
    position = []
    passList = ("123456", "123456789", "12345", "qwerty", "password", "12345678", "111111", "123123", "1234567890", "1234567", "qwerty123", "000000", "1q2w3e", "aa12345678", "abc123", "password1", "1234", "qwertyuiop", "123321", "password123", "1q2w3e4r5t", "iloveyou", "654321", "666666", "987654321", "123", "123456a", "qwe123", "1q2w3e4r", "7777777", "1qaz2wsx", "123qwe", "zxcvbnm", "121212", "asdasd", "a123456", "555555", "dragon", "112233", "123123123", "monkey", "11111111", "qazwsx", "159753", "asdfghjkl", "222222", "1234qwer", "qwerty1", "123654", "123abc")
    for i in passList:
        if checkPass == i:
            position.append(passList.index(i))
            
    if checkPass in passList:
        found = f'Your password is too common. Please consider changing it. Your password was found at:', position
        return found #the return string is a little wonky looking, I spent an unhealthy amount of time trying to fix it to no avail :(
    else:
        notFound = "You have a strong password"
        return notFound

main()