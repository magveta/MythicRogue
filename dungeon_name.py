import random

first = ("Hollow", "Dark", "Foul-smelling", "Most-loathsome", "Hideous", "Solitary", "Old", "Ancient", "Impenetrable", 
     "Gloomy", "Miserable", "Abysmal", "Abyssic", "Cramped", "Confusing", "Bizarre", "Hateful", "Black", "Dreadful", "Grim",
     "Most-repugnant", "Old", "Unconquerable", "Cryptic", "Occult", "Mystifying", "Mystic", "Mystical", "Mythical", "Mythic",
     "Visceral", "Enigmatic", "Bleak", "Malign", 
     )

scnd = ("Castle", "Dungeon", "Dungeon", "Dungeon", "Depths", "Oubliette", "Hole", "Cromlech", "Tomb", "Burial Grounds", "Cavern",
     "Abyss", "Caves", "Grotto", "Crypt", "Dwelling", "Grove", "Barrow", "Halls", "Lair", "Shrine", "Temple",  
     )

third = ("Of Count Dracul", "Of the Wizard", "Of Trolls", "Of Troland", "Of Ghosts", "Of Spirits",
         "Of Old", "Of Ancient Times", "Of the Old Ones", "Of the Dead", "Of the Draugr", "Of Ghouls", "Of Old Ones", "Of Goblins", 
         "Of Dusk", "Of thy Ancestors", "Of magic", "Of Mystery", "Of Pestilence", 
         )

def generate_dungeon_name():
    name = ""
    for word in (first, scnd, third):
        name += random.choice(word) + " "
    return name