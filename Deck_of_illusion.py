import random
answer = True

deck = {"ace of hearts":"Red Dragon", "king of hearts":"Knight and four guards", "queen of hearts":"Succubus or Incubus", "Jack of heart":"Druid", "ten of hearts":"Cloud Giant", "nine of heart":"Ettin", "eight of hearts":"Bugbear", "two of hearts":"Goblin", "ace of diamonds":"Beholder", "king of diamonds":"Archmage and mage Apprentice", "queen of diamonds":"Night Hag", "jack of diamonds":"Assassin", "ten of diamonds":"Fire giant", "nine of diamonds":"Ogre", "eight of diamonds":"Gnoll", "two of diamonds":"Kobold", "ace of spade":"Lich", "king of spade":"Priest and two acolytes", "queen of spade":"Medusa", "jack of spade":"Veteran", "ten of spade":"Frost Giant", "nine of spade":"Troll", "eight of spade":"Hobgoblin", "two of spade":"Goblin", "ace of clubs":"Iron Golem", "king of clubs":"Bandit Captian and three bandits", "queen of clubs":"Erinyes", "jack of clubs":"Berserker", "ten of clubs":"Hill giant", "nine of clubs":"Ogre", "eight of clubs":"Orc", "two of clubs":"Kobold" }

while answer:
    while len(deck) > 0:
        x = random.choice(list(deck.items()))
        print(x)
        x = x [0]
        del deck[x]
        break
    x = input("Do you wish to contine?")
    while True:
        if x.lower() == "yes":
            break
        elif x.lower() == "no":
            answer = False
            break
        else:
            print("answer must yes or no.")