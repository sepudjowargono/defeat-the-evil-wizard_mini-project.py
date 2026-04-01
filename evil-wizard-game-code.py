import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        # Basic attributes every character has
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        
        # Defensive states
        self.shielded = False
        self.evading = False
        
    # Health never goes below 0
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        
    # Main attack method used by all characters
    def attack(self, opponent, bonus=0, attack_name="Attack"):
        # Do nothing if attacker or opponent is already defeated
        if self.health <= 0 or opponent.health <= 0:
            return
        
        # Random damage within a range (includes bonus)
        damage = random.randint(self.attack_power - 5, self.attack_power + 5) + bonus
        
        # Check if the opponent blocks the attack
        if opponent.shielded:
            print(f"{opponent.name} blocked the attack!")
            opponent.shielded = False # Shield only works once
            return
        
        #Check if the opponent evades the attack
        if opponent.evading:
            print(f"{opponent.name} evaded the attack!")
            opponent.evading = False # Evade only works once
            return
        
        # Apply damage
        opponent.take_damage(damage)
        print(f"{self.name} uses {attack_name} on {opponent.name} for {damage} damage!")
        
        # Check if opponent is defeated
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    # Heal method 
    def heal(self, amount=None):
        # Do nothing if health is already depleted
        if self.health <= 0:
            return
            
        if amount is None:
            heal_amount = random.randint(15, 25)
        else:
            heal_amount = amount
        
        old_health = self.health
        # Health does not exceed max health
        self.health = min(self.health + heal_amount, self.max_health)
        actual_heal = self.health - old_health
        
        print(f"{self.name} has healed for {actual_heal} health!")
        
    # Display characters stats
    def display_stats(self):
        print(f"{self.name}")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack Power: {self.attack_power}")
        
# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        
    def power_strike(self, opponent):
        self.attack(opponent, bonus=8, attack_name="Power Strike")
        
    def battle_cry(self):
        if self.health <= 0:
            return
        
        self.attack_power += 8
        print(f"{self.name} uses Battle Cry! Attack power has increased by 8.")
        
# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        
    def fireball(self, opponent):
        self.attack(opponent, bonus=12, attack_name="Fireball")
        
    def magic_barrier(self):
        if self.health <= 0:
            return
        
        self.shielded = True
        print(f"{self.name} activates Magic Barrier and will block the next attack!")
        
# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=28)
        
    def quick_shot(self, opponent):
        if self.health <= 0 or opponent.health <= 0:
            return
        
        print(f"{self.name} uses Quick Shot!")
        
        for i in range(2): #shoots twice
            # Stops if opponent is already defeated
            if opponent.health <= 0:
                break
            
            print(f"Shot {i + 1}:")
            self.attack(opponent, bonus=-5, attack_name="Quick Shot")
            
    def evade(self):
        if self.health <= 0:
            return
        
        self.evading = True
        print(f"{self.name} prepares to evade the next attack!")
        
# Create Paladin class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=22) 
        
    def holy_strike(self, opponent):
        self.attack(opponent, bonus=12, attack_name="Holy Strike")
        
    def divine_shield(self):
        if self.health <= 0:
            return
        
        self.shielded = True
        print(f"{self.name} activates Divine Shield and will block the next attack!")
        
# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)
        
    def regenerate(self):
        if self.health <= 0:
            return
        
        print(f"{self.name} regenerates!")
        self.heal(10)
        
    def dark_spell(self, opponent):
        self.attack(opponent, bonus=8, attack_name="Dark Spell")
        
# Create player character
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")
    
    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)
    
# Special ability handler
def use_ability(player, wizard):
    # Checks player type and shows correct abilities
    if isinstance(player, Warrior):
        print("1. Power Strike")
        print("2. Battle Cry")
        choice = input("Choose ability: ")
        
        if choice == '1':
            player.power_strike(wizard)
        elif choice == '2':
            player.battle_cry()
        else:
            print("Invalid ability choice.")

    elif isinstance(player, Mage):
        print("1. Fireball")  
        print("2. Magic Barrier")
        choice = input("Choose ability: ")
        
        if choice == '1':
            player.fireball(wizard)
        elif choice == '2':
            player.magic_barrier()
        else:
            print("Invalid ability choice.")
        
    elif isinstance(player, Archer):
        print("1. Quick Shot")
        print("2. Evade")
        choice = input("Choose ability: ")
        
        if choice == '1':
            player.quick_shot(wizard)
        elif choice == '2':
            player.evade()
        else:
            print("Invalid ability choice.")
            
    elif isinstance(player, Paladin):
        print("1. Holy Strike")
        print("2. Divine Shield")
        choice = input("Choose ability: ")
        
        if choice == '1':
            player.holy_strike(wizard)
        elif choice == '2':
            player.divine_shield()
        else:
            print("Invalid ability choice.")           

 # Battle system   
def battle(player, wizard):
    # Loop continues until one character is defeated
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")
        
        # Player action
        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            use_ability(player, wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
            wizard.display_stats()
            continue
        else:
            print("Invalid choice. Try again.")
            continue
        
        # Stop if wizard is defeated
        if wizard.health <= 0:
            break
        
        # Wizards turn
        print("\n--- Evil Wizard's Turn ---")
        wizard.regenerate() # Wizard regenerates health at the start of every turn
        
        # Wizard randomly chooses attack type
        wizard_choice = random.choice(["attack", "spell"])
        
        if wizard_choice == "attack":
            wizard.attack(player)
        else:
            wizard.dark_spell(player)
            
        # Stop if player is defeated
        if player.health <= 0:
            print(f"\nDefeat! {player.name} has been defeated by {wizard.name}!")
            break

    # Victory message
    if wizard.health <= 0:
        print(f"\nVictory! {player.name} defeated {wizard.name}!")
        
# Main function
def main():
    print("=" *28)
    print("|| DEFEAT THE EVIL WIZARD ||")
    print("=" *28)
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

# Run the program
if __name__ == "__main__":
    main()    
