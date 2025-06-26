class Person: #the superclass, takes name, address, and phonenumber
    def __init__(self, name, address, phonenumber): #dunder method
        self.name = name
        self.address = address
        self.phonenumber = phonenumber
    
    def set_name(self, name):
        self.name = name
    
    def set_address(self, address):
        self.address = address
    
    def set_phonenumber(self, phonenumber):
        self.phonenumber = phonenumber
        
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def get_phonenumber(self):
        return self.phonenumber
    
class Customer(Person): #subclass nested within the superclass
    def __init__(self, name, address, phonenumber, customernumber, mailing): 
        super().__init__(name, address, phonenumber) #Inherts all attributes from Person superclass
        self.mailing = mailing #next 2 lines assign the attributes special to the customer subclass
        self.customernumber = customernumber
   
def main():
    name = input("What is the customer's name? ") #Next few lines get the values for the attributes, where they are then assigned to their proper super/sub class
    address = input("What is their address? (example address to use: 73 Rainey Street, Arlen, TX): ")
    phonenumber = input("What is their number? (example number to use: 213-258-2858): ")
    customernumber = input("What is their customer number: ")
    mailing = bool(input("Does the customer want to be mailed? Please input True or False: "))

    customer1 = Customer(name, address, phonenumber, customernumber, mailing) #Creates the object customer1 in the Customer subclass
        
    print(f"Your customer's data is: \nname: {customer1.name} \naddress: {customer1.address} \nphone number: {customer1.phonenumber} \ncustomer number: {customer1.customernumber} \non the mailing list: {customer1.mailing}")
    #print statement above gave me a lot of trouble, I referenced lectures and past code, all had different methods of doing it, none of them worked for me lol. Finally got it to work though
    
main()