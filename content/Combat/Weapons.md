- Mechanical descriptions are found here
- Feel free to reflavor the weapons as you wish
- #todo figure out how to do poisons: prolly something along the line of it dealing extra composure damage but against uncomposed targets, it does its effect

# Weight
- An abstraction over both size and weight
- Dictates damage and minimum vitality needed to wield
	- To wield larger weapons, multiply costs by 5
	- All larger weapons are considered **Two Pawed**
- Weapons meant for larger creatures multiply the damage die and inventory slots needed by how many categories above raccoon they are

| Weight | Damage | Minimum Vitality | Inventory Slots |
| ------ | ------ | ---------------- | --------------- |
| Light  | d4     | d4               | Small           |
| Medium | d8     | d8               | Medium          |
| Heavy  | d12    | d12              | Large           |

 
# Traits
- **Backstabbing**. When you attack a creature that is Off-Guard, you double the damage die of the weapon.
- **Cleave**. Your attack hits all enemies in a 180 degree arc in melee range.
- **Charge**. If you move in a straight line for at least 10 meters towards a target before making an attack on them, the damage dice is doubled
- **Grapple**. When you [[Combat Rules#Grapple Attack]] while holding the weapon, your grapple check is also dealt as damage.
- **Powerful**. Increase the weapon’s damage dice by two sizes over the damage defined by size.
- **Push**. When you [[Combat Rules#Shove Attack]], your shove check is also dealt as damage.
- **N-Pawed**. Requires $n$ to wield. If $n$ not specified, assume 1 pawed.
- **Range**. This is a ranged weapon, with range increments of 10 meters. For each range increment past the first one, you gain one additional disadvantage. 
- **Reach**. Adds 1 meter melee range.
- **Thrown**. Has a thrown range increment of 5 meters. For each range increment past the first one, you gain a disadvantage.

## Material Traits
Following traits are mutually exclusive. If not specified, assume some other neolithic material like wood, stone, bone, sinew, etc etc
- **Metal**. Increase damage dice of weapon multiplier by one. 
- **Obsidian**. If any of the dice involved in the attack roll explodes, apply [[Bleeding]] condition to the target. The countdown size is determined by the number of explosions; ie. 1 explosion => Cd4, 2 explosions => Cd6, ... to a max of Cd12. Then weapon die for this weapon decreases by 1 size. The weapon shatters when it goes down from a d4.

# Weapons
- **Javelin**. Light, Polearm, Thrown, Reach
- **Staff**. Medium, Polearm, 2 pawed
- **Spear**. Medium, Polearm, Reach, Charge, 2 pawed
---
- **Light Club**. Light, Impact, Push
- **Club**. Medium, Impact, Push
- **Greatclub**. Heavy, Impact, Push, 2 pawed
---
- **Hatchet**. Light, Impact, Cleave, Versatile
- **Axe**. Medium, Impact, Cleave, Charge
- **Greataxe**. Heavy, Impact, Cleave, Charge, 2 pawed
---
- **Knife**. Light, Blade, Backstabbing, Thrown
---
- **Whip**. Light, Flexible, Grapple, Reach
---

All self bows are large and all horn bows are medium sized items
- **Training Bow**. Light, Bow, Range
- **Hunting Bow**. Medium, Bow, Range
- **War Bow**. Heavy, Bow, Range
	- An **arrow** is a small item, but a **quiver** of 12 arrows is medium
---
- **Sling**. Light, Thrown, Range
	- A **stone** large and heavy enough for a sling is a small item
--- 
- **Boomerang**. Light, Thrown, Range #todo
- **Net**. Heavy, Thrown, Range: Requires two actions to attempt an Athletics/Finesse check against the weapon roll to escape #todo
- **Bolo**. Light, Thrown, Range, Special: Deals only composure damage. Target is [[Restrained]] until someone (including the target) spends an action to free them. 
---
