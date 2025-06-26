import random

class Humanoid:
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.height = height
        self.weight = weight
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

class Humans(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        tag = input("Tag! What attribute do you want to tag? (Enter one of these: strength, dexterity, constitution, intelligence, wisdom, charisma): ")
        if tag.lower() == "strength":
            self.strength = strength + 2
        elif tag.lower() == "dexterity":
            self.strength = strength + 2
        elif tag.lower() == "constitution": 
            self.constitution = constitution + 2
        elif tag.lower() == "intelligence":
            self.intelligence = intelligence + 2
        elif tag.lower() == "wisdom":
            self.wisdom = wisdom + 2
        else:
            self.charisma = charisma + 2

class Elves(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.dexterity = dexterity + 2
        self.charisma = charisma + 2
    caffinated = "Spore coffee! 100% Resistance to Sleep. (can't be put to sleep)"
    
class Dwarves(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.strength = strength + 2
        self.constitution = constitution + 2
        self.charisma = charisma - 2
    battle_hardened = "Battle hardened! 20% Resistance to magic."

def charcterCreation():
    print("War, war never changes. 3 races have survived the apocalypse,")
    race = input("\nWhich are you? (Humans, Elves, Dwarves) ")
    height = int(input("\nWhat is your height? (3ft - 7ft) "))
    weight = int(input("\nWhat is your weight? (60 - 300 lbs) "))
    hair_color = input("\nWhat color hair? ")
    eye_color = input("\nWhat eye color? ")
    strength = random.randint(1,18)
    dexterity = random.randint(1,18)
    constitution = random.randint(1,18)
    intelligence = random.randint(1,18)
    wisdom = random.randint(1,18)
    charisma = random.randint(1,18)
    
    print("\nGenerating stats: ", "\nHeight: ", height, "\nWeght: ", weight, "\nHair Color: ", hair_color, "\nEye Color: ", eye_color, "\nStrength: ", strength, "\nDexterity: ", dexterity, "\nConstitution: ", constitution, "\nIntelligence: ", intelligence, "\nWisdom: ", wisdom, "\nCharisma: ", charisma)
    if race == "Humans":
        player = Humans(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        print(f"\nYour final stats are:\nRace:",race,"\nHeight:",player.height,"\nWeight:",player.weight,"\nHair color:", player.hair_color, "\nEye color:", player.eye_color, "\nStrength:", player.strength, "\nDexterity:", player.dexterity, "\nConstitution:", player.constitution, "\nIntelligence: ", player.intelligence, "\nWisdom: ", player.wisdom, "\nCharisma: ", player.charisma, "\nPerks: Tag!: the attribute of your choice has increased by +2")
    elif race == "Elves":
        player = Elves(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        print(f"\nYour final stats are:\nRace:",race,"\nHeight:",player.height,"\nWeight:",player.weight,"\nHair color:", player.hair_color, "\nEye color:", player.eye_color, "\nStrength:", player.strength, "\nDexterity:", player.dexterity, "\nConstitution:", player.constitution, "\nIntelligence: ", player.intelligence, "\nWisdom: ", player.wisdom, "\nCharisma: ", player.charisma, "\nPerks: ", player.caffinated, " Your Dexterity and Charisma has increased by +2.")
    else:
        player = Dwarves(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        print(f"\nYour final stats are:\nRace:",race,"\nHeight:",player.height,"\nWeight:",player.weight,"\nHair color:", player.hair_color, "\nEye color:", player.eye_color, "\nStrength:", player.strength, "\nDexterity:", player.dexterity, "\nConstitution:", player.constitution, "\nIntelligence: ", player.intelligence, "\nWisdom: ", player.wisdom, "\nCharisma: ", player.charisma, "\nPerks: ", player.battle_hardened, " Your Strength and Constiution has increased by 2, your Charisma has decreased by -2.")

def main():
    charcterCreation()
    
main()