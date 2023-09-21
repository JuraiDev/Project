import random

class Entity:
    def __init__(self, name, entity_type, level=1):
        self.name = name
        self.entity_type = entity_type
        self.level = level
        self.hp = self.level * random.randint(10, 12)
        self.strength = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        self.dexterity = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        self.constitution = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        self.intelligence = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        self.wisdom = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        self.charisma = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        self.skills = {}
        self.inventory = {}
        self.party = None

    def add_to_party(self, party):
        if self.party:
            self.party.remove_member(self)
        party.add_member(self)
        self.party = party

    def remove_from_party(self):
        if self.party:
            self.party.remove_member(self)
            self.party = None

    def attack(self, target):
        attack_roll = random.randint(1, 20) + self.strength
        if attack_roll >= target.get_ac():
            damage = random.randint(1, 8) + self.strength
            target.take_damage(damage)
            print(f"{self.name} attacked {target.name} for {damage} damage!")
        else:
            print(f"{self.name}'s attack missed!")

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.die()

    def die(self):
        print(f"{self.name} has died!")
        if self.party:
            self.party.remove_member(self)

    def get_ac(self):
        return 10 + self.dexterity

    def customize_character(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    # ... (more methods to be added here)

class Party:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, entity):
        if len(self.members) < 4:
            self.members.append(entity)
            print(f"{entity.name} has joined the party {self.name}!")
        else:
            print(f"The party {self.name} is full!")

    def remove_member(self, entity):
        self.members.remove(entity)
        print(f"{entity.name} has left the party {self.name}!")

    # ... (more methods to be added here)

# ... (more classes and methods to be added here)
class Skill:
    def __init__(self, name, description, ability_score, level_required):
        self.name = name
        self.description = description
        self.ability_score = ability_score
        self.level_required = level_required

    def use(self, user, target):
        if user.level >= self.level_required:
            if self.ability_score == 'strength':
                modifier = user.strength
            elif self.ability_score == 'dexterity':
                modifier = user.dexterity
            elif self.ability_score == 'constitution':
                modifier = user.constitution
            elif self.ability_score == 'intelligence':
                modifier = user.intelligence
            elif self.ability_score == 'wisdom':
                modifier = user.wisdom
            elif self.ability_score == 'charisma':
                modifier = user.charisma
            else:
                modifier = 0

            damage = random.randint(1, 8) + modifier
            target.take_damage(damage)
            print(f"{user.name} used {self.name} on {target.name} for {damage} damage!")
        else:
            print(f"{user.name} is not high enough level to use {self.name}!")

class AI:
    def __init__(self, behavior_type):
        self.behavior_type = behavior_type

    def execute_behavior(self, entity, target):
        if self.behavior_type == "aggressive":
            entity.attack(target)
        elif self.behavior_type == "defensive":
            print(f"{entity.name} is defending against {target.name}'s attacks")
        elif self.behavior_type == "friendly":
            print(f"{entity.name} is friendly towards {target.name}")

# ... (existing classes here)

class Entity:
    # ... (existing methods here)

    def learn_skill(self, skill):
        self.skills[skill.name] = skill
        print(f"{self.name} learned a new skill: {skill.name}")

    def use_skill(self, skill_name, target):
        if skill_name in self.skills:
            self.skills[skill_name].use(self, target)
        else:
            print(f"{self.name} has not learned the skill {skill_name}")

    def set_ai(self, ai):
        self.ai = ai

    def execute_ai(self, target):
        self.ai.execute_behavior(self, target)

# ... (existing classes here)

# ... (more methods to be added here)
class InventoryItem:
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

    def use(self, user):
        self.effect(user)
        print(f"{user.name} used {self.name}!")

class Armor:
    def __init__(self, name, defense_bonus):
        self.name = name
        self.defense_bonus = defense_bonus

class Weapon:
    def __init__(self, name, attack_bonus):
        self.name = name
        self.attack_bonus = attack_bonus

class Entity:
    # ... (existing methods here)

    def equip_armor(self, armor):
        self.armor = armor
        print(f"{self.name} equipped {armor.name}!")

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} equipped {weapon.name}!")

    def add_to_inventory(self, item):
        if item.name not in self.inventory:
            self.inventory[item.name] = item
        else:
            print(f"{item.name} is already in the inventory")

    def use_item(self, item_name):
        if item_name in self.inventory:
            self.inventory[item_name].use(self)
        else:
            print(f"{item_name} is not in the inventory")

    def get_ac(self):
        base_ac = 10 + self.dexterity
        if hasattr(self, 'armor'):
            base_ac += self.armor.defense_bonus
        return base_ac

    def attack(self, target):
        attack_roll = random.randint(1, 20) + self.strength
        if hasattr(self, 'weapon'):
            attack_roll += self.weapon.attack_bonus
        if attack_roll >= target.get_ac():
            damage = random.randint(1, 8) + self.strength
            target.take_damage(damage)
            print(f"{self.name} attacked {target.name} for {damage} damage!")
        else:
            print(f"{self.name}'s attack missed!")

# ... (existing classes here)

# ... (more methods to be added here)
class Trait:
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

class Entity:
    # ... (existing methods here)

    def add_trait(self, trait):
        self.traits[trait.name] = trait
        print(f"{self.name} acquired a new trait: {trait.name}")

    def apply_trait_effects(self):
        for trait in self.traits.values():
            trait.effect(self)

class Party:
    # ... (existing methods here)

    def party_attack(self, target):
        for member in self.members:
            member.attack(target)

    def party_use_skill(self, skill_name, target):
        for member in self.members:
            if skill_name in member.skills:
                member.use_skill(skill_name, target)

    def party_use_item(self, item_name, target):
        for member in self.members:
            if item_name in member.inventory:
                member.use_item(item_name, target)

    def distribute_experience(self, amount):
        for member in self.members:
            member.gain_experience(amount)

    def party_status(self):
        for member in self.members:
            print(f"{member.name} - HP: {member.hp}, Level: {member.level}")

# ... (existing classes here)

# ... (more methods to be added here)
class Quest:
    def __init__(self, name, description, objectives, reward):
        self.name = name
        self.description = description
        self.objectives = objectives
        self.reward = reward
        self.completed = False

    def check_completion(self, entity):
        for objective in self.objectives:
            if not objective.check_completion(entity):
                return False
        self.completed = True
        return True

    def grant_reward(self, entity):
        if self.completed:
            self.reward(entity)
            print(f"{entity.name} has completed the quest {self.name} and received the reward!")
        else:
            print(f"The quest {self.name} is not yet completed.")

class Objective:
    def __init__(self, description, condition):
        self.description = description
        self.condition = condition
        self.completed = False

    def check_completion(self, entity):
        if self.condition(entity):
            self.completed = True
        return self.completed

class Entity:
    # ... (existing methods here)

    def gain_experience(self, amount):
        self.experience_points += amount
        print(f"{self.name} gained {amount} experience points!")
        while self.experience_points >= self.level * 100:
            self.experience_points -= self.level * 100
            self.level_up()

    def level_up(self):
        self.level += 1
        self.hp += random.randint(1, 8) + self.constitution
        print(f"{self.name} leveled up to level {self.level}!")

    def accept_quest(self, quest):
        self.quests[quest.name] = quest
        print(f"{self.name} accepted the quest {quest.name}!")

    def complete_quest(self, quest_name):
        if quest_name in self.quests:
            quest = self.quests[quest_name]
            if quest.check_completion(self):
                quest.grant_reward(self)
                del self.quests[quest_name]
        else:
            print(f"{self.name} has not accepted the quest {quest_name}")

# ... (existing classes here)

# ... (more methods to be added here)
class Dialogue:
    def __init__(self, text, responses):
        self.text = text
        self.responses = responses

class Response:
    def __init__(self, text, effect=None):
        self.text = text
        self.effect = effect

class Entity:
    # ... (existing methods here)

    def initiate_dialogue(self, dialogue):
        print(dialogue.text)
        for i, response in enumerate(dialogue.responses):
            print(f"{i+1}. {response.text}")
        choice = int(input("Choose a response: ")) - 1
        if 0 <= choice < len(dialogue.responses):
            if dialogue.responses[choice].effect:
                dialogue.responses[choice].effect(self)
        else:
            print("Invalid choice.")

    def add_item_to_inventory(self, item):
        self.inventory[item.name] = item
        print(f"{self.name} added {item.name} to their inventory.")

    def equip_item(self, item_name):
        if item_name in self.inventory:
            item = self.inventory[item_name]
            if isinstance(item, Armor):
                self.equip_armor(item)
            elif isinstance(item, Weapon):
                self.equip_weapon(item)
            else:
                print(f"{item_name} cannot be equipped.")
        else:
            print(f"{item_name} is not in the inventory.")

    def interact_with_entity(self, other_entity):
        if hasattr(other_entity, 'dialogue'):
            self.initiate_dialogue(other_entity.dialogue)
        else:
            print(f"{other_entity.name} has nothing to say.")

# ... (existing classes here)

# ... (more methods to be added here)
class Ability:
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

    def use(self, user, target=None):
        self.effect(user, target)
        print(f"{user.name} used {self.name}!")

class Entity:
    # ... (existing methods here)

    def learn_ability(self, ability):
        self.abilities[ability.name] = ability
        print(f"{self.name} learned a new ability: {ability.name}")

    def use_ability(self, ability_name, target=None):
        if ability_name in self.abilities:
            self.abilities[ability_name].use(self, target)
        else:
            print(f"{self.name} has not learned the ability {ability_name}")

    def create_party(self, members):
        self.party = Party(members)
        print(f"{self.name} created a party with {', '.join([member.name for member in members])}")

    def join_party(self, party):
        party.add_member(self)
        print(f"{self.name} joined the party")

    def leave_party(self, party):
        party.remove_member(self)
        print(f"{self.name} left the party")

class Party:
    # ... (existing methods here)

    def add_member(self, member):
        self.members.append(member)
        print(f"{member.name} joined the party")

    def remove_member(self, member):
        self.members.remove(member)
        print(f"{member.name} left the party")

# ... (existing classes here)

# ... (more methods to be added here)
class NPC(Entity):
    def __init__(self, name, level, hp, strength, dexterity, constitution, intelligence, wisdom, charisma, dialogue=None):
        super().__init__(name, level, hp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.dialogue = dialogue
        self.quests_given = []

    def give_quest(self, quest, player):
        if quest not in self.quests_given:
            player.accept_quest(quest)
            self.quests_given.append(quest)
            print(f"{self.name} gave {player.name} a quest: {quest.name}")

    def ai_behavior(self, player):
        if self.dialogue:
            player.initiate_dialogue(self.dialogue)
        else:
            print(f"{self.name} has nothing to say.")

class Monster(Entity):
    def __init__(self, name, level, hp, strength, dexterity, constitution, intelligence, wisdom, charisma, abilities):
        super().__init__(name, level, hp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.abilities = abilities

    def ai_behavior(self, player):
        if self.hp <= 0:
            print(f"{self.name} is dead and cannot act.")
        else:
            if random.random() < 0.5:
                self.attack(player)
            else:
                ability_name = random.choice(list(self.abilities.keys()))
                self.use_ability(ability_name, player)

# ... (existing classes here)

def game_loop(player, entities):
    while player.hp > 0:
        print(f"\n{player.name}'s turn:")
        action = input("Choose an action (attack, use ability, use item, interact): ").strip().lower()
        if action == "attack":
            target_name = input("Choose a target: ").strip()
            target = next((entity for entity in entities if entity.name == target_name), None)
            if target:
                player.attack(target)
            else:
                print("Invalid target.")
        elif action == "use ability":
            ability_name = input("Choose an ability: ").strip()
            target_name = input("Choose a target: ").strip()
            target = next((entity for entity in entities if entity.name == target_name), None)
            if target:
                player.use_ability(ability_name, target)
            else:
                print("Invalid target.")
        elif action == "use item":
            item_name = input("Choose an item: ").strip()
            player.use_item(item_name)
        elif action == "interact":
            target_name = input("Choose an entity to interact with: ").strip()
            target = next((entity for entity in entities if entity.name == target_name), None)
            if target:
                player.interact_with_entity(target)
            else:
                print("Invalid entity.")
        else:
            print("Invalid action.")

        for entity in entities:
            if isinstance(entity, NPC) or isinstance(entity, Monster):
                entity.ai_behavior(player)

        if player.hp <= 0:
            print(f"{player.name} has died.")
            break

# ... (more methods to be added here)
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity=1):
        if item.name in self.items:
            self.items[item.name]['quantity'] += quantity
        else:
            self.items[item.name] = {'item': item, 'quantity': quantity}
        print(f"Added {quantity} {item.name}(s) to the inventory.")

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items and self.items[item_name]['quantity'] >= quantity:
            self.items[item_name]['quantity'] -= quantity
            if self.items[item_name]['quantity'] == 0:
                del self.items[item_name]
            print(f"Removed {quantity} {item_name}(s) from the inventory.")
        else:
            print(f"Not enough {item_name}(s) in the inventory.")

    def use_item(self, item_name, target):
        if item_name in self.items and self.items[item_name]['quantity'] > 0:
            item = self.items[item_name]['item']
            item.use(target)
            self.remove_item(item_name)
        else:
            print(f"No {item_name}(s) available in the inventory.")

class Item:
    def __init__(self, name, description, use_effect=None):
        self.name = name
        self.description = description
        self.use_effect = use_effect

    def use(self, target):
        if self.use_effect:
            self.use_effect(target)
            print(f"{self.name} was used on {target.name}.")

# ... (existing classes here)

class Entity:
    def __init__(self, name, level, hp, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.name = name
        self.level = level
        self.hp = hp
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def attack(self, target):
        damage = self.strength - target.constitution
        target.hp -= max(0, damage)
        print(f"{self.name} attacked {target.name} for {max(0, damage)} damage")

class Party:
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def is_active(self):
        return any(member.hp > 0 for member in self.members)

    def get_active_members(self):
        return [member for member in self.members if member.hp > 0]

class CombatSystem:
    def __init__(self):
        self.combat_log = []

    def engage(self, party1, party2):
        while party1.is_active() and party2.is_active():
            for member in party1.members:
                if party2.is_active():
                    target = random.choice(party2.get_active_members())
                    member.attack(target)
                    self.combat_log.append(f"{member.name} attacked {target.name}")
                else:
                    break

            for member in party2.members:
                if party1.is_active():
                    target = random.choice(party1.get_active_members())
                    member.attack(target)
                    self.combat_log.append(f"{member.name} attacked {target.name}")
                else:
                    break

        if party1.is_active():
            print(f"Party {party1.name} wins!")
        else:
            print(f"Party {party2.name} wins!")

        for log in self.combat_log:
            print(log)

def main():
    player = Entity("Player", 1, 100, 10, 10, 10, 10, 10, 10)
    npc1 = Entity("NPC1", 1, 50, 8, 8, 8, 8, 8, 8)
    monster1 = Entity("Monster1", 5, 80, 12, 12, 12, 12, 12, 12)
    monster2 = Entity("Monster2", 3, 60, 10, 10, 10, 10, 10, 10)

    party1 = Party("Heroes", [player, npc1])
    party2 = Party("Monsters", [monster1, monster2])

    combat_system = CombatSystem()
    combat_system.engage(party1, party2)

if __name__ == "__main__":
    main()

class Quest:
    def __init__(self, name, description, objectives, reward):
        self.name = name
        self.description = description
        self.objectives = objectives
        self.reward = reward
        self.completed = False

    def check_completion(self, player):
        if all(objective.check_completion(player) for objective in self.objectives):
            self.completed = True
            player.receive_reward(self.reward)
            print(f"{player.name} completed the quest: {self.name}")

class Objective:
    def __init__(self, description, condition):
        self.description = description
        self.condition = condition
        self.completed = False

    def check_completion(self, player):
        if self.condition(player):
            self.completed = True
            print(f"{player.name} completed the objective: {self.description}")

class Reward:
    def __init__(self, experience_points, items):
        self.experience_points = experience_points
        self.items = items

    def grant(self, player):
        player.experience_points += self.experience_points
        for item in self.items:
            player.inventory.add_item(item)
        print(f"{player.name} received {self.experience_points} experience points and {', '.join([item.name for item in self.items])}")

class Entity:
    # ... (existing methods here)

    def accept_quest(self, quest):
        self.active_quests.append(quest)
        print(f"{self.name} accepted the quest: {quest.name}")

    def complete_quest(self, quest):
        quest.check_completion(self)
        if quest.completed:
            self.completed_quests.append(quest)
            self.active_quests.remove(quest)

    def receive_reward(self, reward):
        reward.grant(self)

# ... (existing classes here)

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Objective:
    def __init__(self, description, condition):
        self.description = description
        self.condition = condition
        self.completed = False

    def check_completion(self, player):
        self.completed = self.condition(player)

class Reward:
    def __init__(self, gold, items):
        self.gold = gold
        self.items = items

    def grant(self, player):
        player.gold += self.gold
        player.inventory.extend(self.items)

class Quest:
    def __init__(self, name, description, objectives, reward):
        self.name = name
        self.description = description
        self.objectives = objectives
        self.reward = reward
        self.completed = False

    def check_completion(self, player):
        self.completed = all(objective.check_completion(player) for objective in self.objectives)
        if self.completed:
            player.receive_reward(self.reward)

class Entity:
    # ... (existing methods here)
    def __init__(self):
        self.name = "Player"
        self.monsters_defeated = 0
        self.gold = 0
        self.inventory = []
        self.active_quests = []
        self.completed_quests = []

    # ... (methods accept_quest, complete_quest, receive_reward as in your snippet)

# ... (existing classes here)

def main():
    # ... (existing setup here)
    item_potion = Item("Potion", "Restores 50 HP")
    item_sword = Item("Sword", "A sharp blade")

    quest_objective1 = Objective("Defeat 5 monsters", lambda player: player.monsters_defeated >= 5)
    quest_reward1 = Reward(100, [item_potion, item_sword])
    quest1 = Quest("Monster Slayer", "Defeat 5 monsters in the forest", [quest_objective1], quest_reward1)

    player = Entity()
    player.accept_quest(quest1)

    # ... (more gameplay logic here)

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
class Dialogue:
    def __init__(self, lines):
        self.lines = lines

    def initiate(self, player, npc):
        for line in self.lines:
            speaker = player if line['speaker'] == 'player' else npc
            print(f"{speaker.name}: {line['text']}")
            if 'response_options' in line:
                for i, option in enumerate(line['response_options']):
                    print(f"{i+1}. {option['text']}")
                choice = int(input("Choose a response: ")) - 1
                if 'effect' in line['response_options'][choice]:
                    line['response_options'][choice]['effect'](player, npc)

class Shop:
    def __init__(self, items):
        self.items = items

    def open_shop(self, player):
        while True:
            print("Shop Inventory:")
            for i, item in enumerate(self.items):
                print(f"{i+1}. {item.name} - {item.description}")
            print(f"{len(self.items)+1}. Exit")
            choice = int(input("Choose an item to buy: ")) - 1
            if choice == len(self.items):
                break
            elif 0 <= choice < len(self.items):
                player.buy_item(self.items[choice])
            else:
                print("Invalid choice.")

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item.name} to inventory.")

class Dialogue:
    def __init__(self, lines):
        self.lines = lines

    def initiate(self, entity, npc):
        for line in self.lines:
            print(line.format(entity_name=entity.name, npc_name=npc.name))

class NPC:
    def __init__(self, name):
        self.name = name

class Entity:
    # ... (existing methods here)
    def __init__(self, name, gold):
        self.name = name
        self.gold = gold
        self.inventory = Inventory()

    def initiate_dialogue(self, dialogue, npc):
        dialogue.initiate(self, npc)

    def buy_item(self, item):
        if self.gold >= item.price:
            self.gold -= item.price
            self.inventory.add_item(item)
            print(f"{self.name} bought {item.name} for {item.price} gold.")
        else:
            print(f"{self.name} does not have enough gold to buy {item.name}.")

# ... (existing classes here)

def main():
    # ... (existing setup here)
    player = Entity("Player", 100)
    npc = NPC("Shopkeeper")
    dialogue = Dialogue(["{entity_name}: Hello, {npc_name}!", "{npc_name}: Welcome to my shop, {entity_name}!"])
    sword = Item("Sword", 50)

    player.initiate_dialogue(dialogue, npc)
    player.buy_item(sword)

    # ... (more gameplay logic here)

if __name__ == "__main__":
    main()


# ... (existing classes here)
class Quest:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def assign_to(self, player):
        player.quests.append(self)
        print(f"{player.name} has accepted the quest: {self.name}")

class Shop:
    def __init__(self, items):
        self.items = items

    def open_shop(self, player):
        for item in self.items:
            print(f"{item.name} - {item.price} gold")
        # ... (more shop logic here)

class NPC:
    def __init__(self, name, quests, shop):
        self.name = name
        self.quests = quests
        self.shop = shop

    def give_quest(self, quest, player):
        quest.assign_to(player)

    def initiate_dialogue(self, dialogue):
        for line in dialogue.lines:
            print(line["text"])
            for option in line["response_options"]:
                print(f"- {option['text']}")
            # ... (more dialogue logic here)

class Dialogue:
    def __init__(self, lines):
        self.lines = lines

# ... (existing classes here)

def main():
    # ... (existing setup here)
    quest1 = Quest("Goblin Hunt", "Defeat 10 goblins in the forest")
    shop_items = [Item("Sword", 50), Item("Shield", 30)]  # Assuming Item class is defined elsewhere
    shop = Shop(shop_items)
    npc = NPC("Village Elder", [quest1], shop)

    dialogue_lines = [
        {"speaker": "npc", "text": "Hello, adventurer. How can I help you today?", "response_options": [
            {"text": "Do you have any quests for me?", "effect": lambda player, npc: npc.give_quest(quest1, player)},
            {"text": "What do you have for sale?", "effect": lambda player, npc: shop.open_shop(player)},
            {"text": "Goodbye.", "effect": lambda player, npc: print(f"{npc.name}: Goodbye, {player.name}.")}
        ]},
        # ... (more dialogue lines here)
    ]
    dialogue = Dialogue(dialogue_lines)
    npc.initiate_dialogue(dialogue)

    # ... (more gameplay logic here)

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
class AI:
    def __init__(self, behavior_tree):
        self.behavior_tree = behavior_tree

    def execute_behavior(self, entity, world_state):
        self.behavior_tree.execute(entity, world_state)

class BehaviorNode:
    def execute(self, entity, world_state):
        pass

class SelectorNode(BehaviorNode):
    def __init__(self, children):
        self.children = children

    def execute(self, entity, world_state):
        for child in self.children:
            if child.execute(entity, world_state):
                return True
        return False

class SequenceNode(BehaviorNode):
    def __init__(self, children):
        self.children = children

    def execute(self, entity, world_state):
        for child in self.children:
            if not child.execute(entity, world_state):
                return False
        return True

class ActionNode(BehaviorNode):
    def __init__(self, action):
        self.action = action

    def execute(self, entity, world_state):
        return self.action(entity, world_state)

# ... (existing classes here)

class Entity:
    # ... (existing methods here)

    def set_ai(self, ai):
        self.ai = ai

    def update(self, world_state):
        if self.ai:
            self.ai.execute_behavior(self, world_state)

# ... (existing classes here)

class ActionNode:
    def __init__(self, action):
        self.action = action

    def evaluate(self, entity, world_state):
        return self.action(entity, world_state)

class SelectorNode:
    def __init__(self, children):
        self.children = children

    def evaluate(self, entity, world_state):
        for child in self.children:
            if child.evaluate(entity, world_state):
                return True
        return False

class AI:
    def __init__(self, root_node):
        self.root_node = root_node

    def update(self, world_state, entity):
        self.root_node.evaluate(entity, world_state)

class Entity:
    def __init__(self, name):
        self.name = name
        self.ai = None

    def set_ai(self, ai):
        self.ai = ai

    def update(self, world_state):
        if self.ai:
            self.ai.update(world_state, self)

# ... (existing classes here)

def main():
    # ... (existing setup here)
    player = Entity("Player")
    monster = Entity("Monster")

    def wander_action(entity, world_state):
        # ... (logic for wandering action here)
        print(f"{entity.name} is wandering.")
        return True

    def seek_player_action(entity, world_state):
        # ... (logic for seeking player action here)
        print(f"{entity.name} is seeking the player.")
        return True

    wander_node = ActionNode(wander_action)
    seek_player_node = ActionNode(seek_player_action)
    root_node = SelectorNode([seek_player_node, wander_node])

    monster_ai = AI(root_node)
    monster.set_ai(monster_ai)

    world_state = {}
    while True:
        # ... (game loop logic here)
        player.update(world_state)
        monster.update(world_state)
        # ... (more game loop logic here)

if __name__ == "__main__":
    main()
