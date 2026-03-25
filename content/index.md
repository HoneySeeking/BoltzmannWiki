# TLDR
- High lethality & low(ish) power system, with fast, furious, and swingy combat
- Character progression is less in width of power but in breadth of power
- Hopefully these 2 combined create a system that's less about stacks of hp bonking each other until one falls, and more about a system where (fair) combat is the last resort and more about getting through problems creatively
- Increasing die sizes and numbers are used in place of modifiers, so I recommend having multiple sets of dice on hand, ideally 3 to 5 sets
- As this is all playtest material, everything is subject to change (perhaps drastically) mid-session or session-to-session
	- If you see the #todo tag anywhere, assume whatever it's attached to isn't canon unless you wanna help me flush out that specific system with ideas of your own

# Essential Articles
> Stuff that looks like this are flavor text/lore dumps and don't contain info pertaining to game mechanics

- [[Intro]]
- [[Character Creation]]
- [[Magic]]
- [[Divergent Spin]]
- [[Combat Rules]]
- [[Languages]]
- [[Inventory]]

# General Mechanics
- Advantage/Disadvantage is a stacking ±4 modifier to the roll
- If unspecified always assume round up
- [[Conditions]]
- [[Damage]] types
- [[Movement]]
- [[Size]]
- Torches burn for 30 minutes real time

## Character Sheet
- Still a work in progress, but channeling might be a lil tricky => few ideas:
	- push the sticky deeper into your character sheet to indicate you're channeling it
	- for attribute/skill dice, show how your base value is modified with something a "d6 -> d10" type notation
	- write the traits you get from channeling from the bottom up/or in a pencil
- Cross out/draw a harder line delineating your carry capacity

## Exploding Dice
- Reroll and add the result of any max rolls for as many times it happens. Applies to all the dice involved in a roll
- Below are monte-carlo estimations (n=1,000,000) for expected value and variance:

Normal Dice:

|Dice|Mean|Std Dev|
|---|---|---|
|d4|2.50|1.12|
|d6|3.50|1.71|
|d8|4.50|2.29|
|d10|5.51|2.87|
|d12|6.50|3.45|
|d20|10.51|5.77|

Exploding Dice:

| Dice |  Mean | Std Dev | Max |
| ---: | ----: | ------: | --: |
|   d4 |  3.33 |    2.79 |  42 |
|   d6 |  4.19 |    3.25 |  45 |
|   d8 |  5.14 |    3.81 |  55 |
|  d10 |  6.11 |    4.36 |  59 |
|  d12 |  7.10 |    4.94 |  73 |
|  d20 | 11.06 |    7.23 |  99 |
## Non-Exploding Dice
- By default all dice of the /(0-9)+d(0-9)+ notation is considered to be exploding
- Normal non exploding rolls will be notated as /(0-9)+D(0-9)+, eg 1D20 or 3D6 with a capital D

## Countdown Dice
- Cd# notation is used for countdown dice, where the countdown is **incremented** at specified interval, rolling the associated dice, with the size of the countdown going down on a 1
- Unless specified otherwise, if something lasts for CdX turns, roll countdown at end of turn
- 1 on a Cd4 ends the countdown
- eg. [[Burning]] for Cd6. Turn 1 rolls 5, taking 5 damage. Turn 2 rolls 1, taking 1 damage, and the dice going down to Cd4. Turn 3 rolls 4, taking 4 damage. Turn 4 rolls 1, taking 1 damage and ending the countdown
- Below are monte-carlo estimations (n=1,000,000) for expected value and variance:

Non-Cumulative Countdown Dice:

| Die | # of rolls | Sum   | Std Dev of Total |
| --- | ---------- | ----- | ---------------- |
| d4  | 4.00       | 9.99  | 10.49            |
| d6  | 6.00       | 20.98 | 22.13            |
| d8  | 8.00       | 36.00 | 37.73            |
| d10 | 10.00      | 55.01 | 57.53            |
| d12 | 11.99      | 77.92 | 81.00            |

Cumulative Countdown Dice:

| Die | # of rolls | Sum    |
| --- | ---------- | ------ |
| d4  | 4.00       | 9.99   |
| d6  | 9.99       | 30.97  |
| d8  | 17.99      | 66.97  |
| d10 | 27.99      | 121.98 |
| d12 | 39.98      | 199.90 |
