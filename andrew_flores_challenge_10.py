class PlayerCharacter():
    def __init__(self, health, armor_rating, attack_power): #defining the dunder method with health, armor_rating and attack_power, all attached to self
            
        self.health = health
        self.armor_rating = armor_rating
        self.attack_power = attack_power
        
    def set_health(self, health): #sets health (the variable in __init__) to whatever health (line 36) is. Also checks to make sure it's within the specified range
        if(health < 0 or health > 100):
            print("health must be from 1-100")
            exit()
        self.health = health
        
    def set_armor_rating(self, armor_rating): #sets armor_rating (the variable in __init__) to whatever armor_rating (line 37) is. Also checks to make sure it's within the specified range
        if(armor_rating < 0 or armor_rating > 20):
            print("armor_rating must be from 1-20")
            exit()
        self.armor_rating = armor_rating
        
    def set_attack_power(self, attack_power): #sets attack_power (the variable in __init__) to whatever attack_power (line 38) is. Also checks to make sure it's within the specified range
        if(attack_power < 0 or attack_power > 20):
            print("attack power must be from 1-20")
            exit()
        self.attack_power = attack_power
        
    def get_health(self): #gets the value of health through self, which is associated not just with the dunder method, but also with health.
        return self.health
    
    def get_armor_rating(self): #gets the value of armor_rating through self, which is associated not just with the dunder method, but also with armor_rating.
        return self.armor_rating 
    
    def get_attack_power(self): #gets the value of attack_power through self, which is associated not just with the dunder method, but also with attack_power.
        return self.attack_power

def main():
    health = int(input("Enter health > ")) #the next 3 lines gets the user's input for the attributes
    armor_rating = int(input("Enter armor rating > "))
    attack_power = int(input("Enter attack power > "))
    wizard = PlayerCharacter(0, 0, 0) #creates the subclass wizard as a PlayerCharacter class with a base slate
    wizard.set_health(health) #calls set_health and sets it to wizard 
    wizard.set_armor_rating(armor_rating) #calls set_armor_rating and sets it to wizard
    wizard.set_attack_power(attack_power) #calls set_attack_power and sets it to wizard
    print(f"Your stats are:\nHealth: {wizard.get_health()}\nArmor Rating: {wizard.get_armor_rating()}\nAttack power: {wizard.get_attack_power()}") #prints out all attributes assuming none have gone over the limit
    
main()