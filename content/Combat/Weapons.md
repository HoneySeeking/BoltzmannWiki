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
| Light  | d4     | d4               | 1               |
| Medium | d8     | d8               | 1               |
| Heavy  | d12    | d12              | 2               |

 
# Traits
- **Backstabbing**. When you attack a creature that is Off-Guard, you double the damage die of the weapon.
- **Cleave**. When you attack, the attack also applies to all enemies within a 180° arc in melee range.
- **Charge**. If you move at least 10 m in a straight line toward a target before attacking, double the weapon damage die.
- **Grapple**. When you [[Combat Rules#Grapple Attack|grapple]] while holding the weapon, your grapple check is also dealt as damage.
- **Powerful**. Increase the weapon’s damage dice by two sizes.
- **Push**. When you [[Combat Rules#Shove Attack|shove]], your shove check is also dealt as damage.
- **Paws** ($n$). Requires $n$ to wield. If $n$ not specified, assume 1 pawed.
- **Range** (10). This is a ranged weapon, with range increments of 10 meters. For each range increment past the first one, you gain one additional disadvantage. 
- **Reach**. Adds 1 meter melee range.
- **Thrown** (5). Has a thrown range increment of 5 meters. For each range increment past the first one, you gain a disadvantage.

## Material Traits
Following traits are mutually exclusive. If not specified, assume some other neolithic material like wood, stone, bone, sinew, etc etc
- **Metal**. Increase damage dice of weapon multiplier by one. 
- **Obsidian**. If any of the dice involved in the attack roll explodes, apply [[Bleeding]] condition to the target. The countdown size is determined by the number of explosions; ie. 1 explosion => Cd4, 2 explosions => Cd6, ... to a max of Cd12. Then weapon die for this weapon decreases by 1 size. The weapon shatters when it goes down from a d4.

# Weapons

## Bladed
- **Knife**. Light, Backstabbing, Thrown (5)

## Bow
All self bows are large and all horn bows are medium sized items. **Quiver** holding 12 arrows is 1 slot
- **Training Bow**. Light, Range (10)
- **Hunting Bow**. Medium, Range (10)
- **War Bow**. Heavy, Range (10)

## Flexible
- **Whip**. Light, Grapple, Reach
- **Hook**. Medium, Grapple, Reach
- **Flail**. Heavy, Grapple, Reach

## Impact
- **Light Club**. Light, Push
- **Club**. Medium, Push
- **Greatclub**. Heavy, Push, Paws (2)
- 
- **Tomahawk**. Light, Cleave
- **Axe**. Medium, Cleave, Charge
- **Greataxe**. Heavy, Cleave, Charge, Paws (2)

## Polearms
- **Javelin**. Light, Thrown (5), Reach
- **Staff**. Medium, 2 pawed
- **Spear**. Medium, Reach, Charge, Paws (2)

## Thrown
- **Atlatl**. Light, Thrown (5)  #todo
- **Boomerang**. Light, Thrown (5), Range #todo
- **Sling**. Light, Thrown (15)
- 
- **Bolo**. Light, Thrown, Range, Special: Deals only composure damage. Target is [[Restrained]] until someone (including the target) spends an action to free them. 
- **Net**. Medium, Thrown, Range, Special: Deals only composure damage. Target is [[Restrained]] until someone (including the target) spends two actions to free them.