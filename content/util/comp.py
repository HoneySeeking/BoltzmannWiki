
def dice_to_tier(dice):
    if dice == 4:
        return 1
    elif dice == 6:
        return 2
    elif dice == 8:
        return 3
    elif dice == 10:
        return 4
    elif dice == 12:
        return 5

def dice_to_comp(dices):
    tiers = [dice_to_tier(dice) for dice in dices]
    
    return tiers[0]*4 + tiers[1]*2 + tiers[2]*4 + tiers[3]*2


print(dice_to_comp([8, 12, 8,6]))
print(dice_to_comp([6, 12, 4,4]))
