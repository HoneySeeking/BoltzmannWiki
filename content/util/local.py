import random

traits = [
    # copy all traits here, or load from file
    "Aquatic", "Big", "Burrowing", "Breath Weapon", "Cone", "Aura", "Catlike Reflexes", "Camouflage", "Chlorophyl", "Complex Pheromones", "Echolocation", "Enhanced Adrenaline",
    "Exceptional Hearing", "Exceptional Smell and Taste", "Exceptional Sight", "Flight-Limited", "Flight", "Leaper", "Left Pawed", "Naturally Armored", "Natural Weapon", "Prehensile Tail/Secondary Arms", "Quick", "Regeneration",
    "Resistance", "Sleep Reduction", "Spiky", "Seismicsense", "Tough", "Unyielding", "Bonus", "Cyclops", "Damage Weakness", "Damage Aversion", "Deformed", "Environmental Weakness",
    "Dependency", "Frail", "Tailless", "Yielding", "Small", "Slow", "Reliable Talent", "Actor", "Henchkeeper", "Racism", "Webspeak", "Bolt",
    "Imbue", "Pheromone", "Line", "Sphere", "Fine Control", "Totem Identification", "Great Healer", "Alert", "David", "Cleaver", "Dual Wielder", "Extra Attack",
    "Exploit Weakness", "Formation Fighter", "Goliath", "Indomitable", "Killing Blow", "Lightning Reflexes", "Powerful Drag", "Second Wind", "Backstab", "Chicanery", "Invisible in Water", "Amorphous.",
    "Heated Body", "Immortality", "Demonic Hunger", "Demonic Illumination", "Demonic Presence", "Masked Pheromones", "Shapechanger", "Synesthesia", "Scentless", "Troll Regeneration", "Legendary Resillience", "Spell Effect",
    "Spirit Sense", "Palinopsia", "Sunlight Weakness", "Tormented", "Totem-Bound"
]

effects = [
    "Acid", "Auditory Illusion", "Blink", "Calm", "Compose", "Conceal", "Confuse", "Control Plants", "Dominate", "Darkness", "Enhance", "Enlarge",
    "Fear", "Fire", "Fog", "Freeze", "Glamor", "Glow", "Hasten", "Levitate", "Life Leech", "Mute", "Natural Weapons", "Paralyze",
    "Protection", "Reduce", "Regenerate", "Resistance", "Restrain", "Rough Terrain", "Rumbling", "Shapechange", "Share Trait", "Simple Command", "Sleep", "Slow",
    "Spark", "Suggest", "Truth", "Visual Illusion", "Water", "Wind"
]

skills = [
    "Vitality", "Agility", "Presence", "Intelligence", "Athletics", "Finesse", "History", "Shivers",
    "Nature", "Persuasion", "Performance", "Perception", "Shamanism", "Stealth", "Alchemy", "Clayworking",
    "Cooking", "Leatherworking", "Painting", "Woodcarving", "Weaving", "An instrument of your choice", "Bladed", "Impact",
    "Polearm", "Flexible", "Bow", "Thrown"
]

minor_offerings = [
    "Burn fragrant herbs or incense. Spirits enjoy the scent, particularly those of the wind, hearth, or sky.",
    "Burn a piece of meat, fish, or bread as a meal for the spirit.",
    "Make a painting depicting it, preferably somewhere it will last. Beat 4d6 on a Painting check.",
    "Carve a representation of the spirit into wood and leave it somewhere meaningful. Beat 4d6 on a Woodcarving check.",
    "Carve a representation of the spirit into stone or bone and leave it somewhere meaningful. Beat 4d6 on a Stoneworking check.",
    "Compose a song in the spirit's name and sing it out to multiple parties. Beat 4d6 on a Performance or an instrument check.",
    "Let the spirit witness a secret. Speak something deeply personal aloud in its presence. It will hold your words, whether as a confidant or blackmailer.",
    "Tend to the spirit’s physical presence. Water a tree, clean a shrine, repair a bridge, or drive out an intruder disrupting the area.",
    "Leave/Scatter/Bury something valuable to you by the spirit's physical presence.",
    "Hunt and offer a small animal to the spirit. Some spirits may require it be cooked, others raw, and some demand the first bite but all demand it be fresh.",
    "Spread your own blood on a stone, tree, or site important to the spirit, gaining 1 [[Wound]].",
    "The spirit unusually hungry today; roll on the Major Spirit Offering Table."
]

major_offerings = [
    "The spirit is unusually chill today; roll on the minor spirit offering table.",
    "Offer the blood of a great beast, something that required struggle to bring down (a large stag, bear, or even a monster).",
    "Permanently part with a treasured item, something of personal or cultural significance.",
    "Undergo a ritual branding, scarification, or tattoo that marks tying you to the spirit.",
    "A sentient creature sacrifice",
    "1d4 sentient creature sacrifice",
    "The spirit unusually hungry today; roll on the Minor Deity Offering Table."
]

def choose_offering():
    # 50/50 chance for minor or major offering, or always use minor/major as you wish
    if random.choice([True, False]):
        offering = random.choice(minor_offerings)
        offering_type = "Minor"
    else:
        offering = random.choice(major_offerings)
        offering_type = "Major"
    return offering_type, offering

def main():
    for i in range(8):
        print("============================")
        trait = random.choice(traits)
        effect = random.choice(effects)
        skill = random.choice(skills)
        # offering_type, offering = choose_offering()
        minor = random.choice(minor_offerings)
        major = random.choice(major_offerings)

        print(f"Random Trait: {trait}")
        print(f"Random Effect: {effect}")
        print(f"Random Skill: {skill}")
        print(f"Minor: {minor}")
        print(f"Major: {major}")

if __name__ == "__main__":
    main()

